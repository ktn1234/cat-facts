from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django_q.tasks import async_task
from django_q.models import OrmQ
from .services import CatFacts
from .tasks import get_cat_facts_task
from .models import CatFactTask, CatFactStatus

def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        task_id = async_task(get_cat_facts_task, hook='catfactsapp.hooks.print_result') # Uncomment this line to test successful task
        # task_id = async_task(get_cat_facts_task, True, hook='catfactsapp.hooks.print_result') # Uncomment this line to test failed task
        print(f'Task ID: {task_id}')
        queue_tasks = OrmQ.objects.all()
        for queue_task in queue_tasks:
            if queue_task.task_id() == task_id:
                cat_fact_task = CatFactTask(
                    id=task_id,
                    result=None,
                    status=CatFactStatus.IN_PROGRESS.value,
                    started=queue_task.lock,
                    completed=None,
                    task=None
                )
                cat_fact_task.save()

    # tasks = Task.objects.all() # Successful/Failed tasks
    # queue = OrmQ.objects.all() # Queued tasks

    # tasks = [{'id': task.id, 'result': task.result, 'status': 'Done', 'started': task.started, 'completed': task.stopped} for task in tasks]
    # queue = [{'id': task.task_id(), 'result': 'In Progress...', 'status': 'Running', 'started': task.lock, 'completed': None} for task in queue]
    # tasks.extend(queue)

    # tasks.sort(key=lambda task: task["started"], reverse=True)

    cat_fact_tasks = CatFactTask.objects.all().order_by('-started')
    return render(request, 'catfactsapp/index.html', {'cat_fact_tasks': cat_fact_tasks})

def index_delete(request: HttpRequest, task_id: str) -> HttpResponse:
    try:
        cat_fact = CatFactTask.objects.get(id=task_id)
        cat_fact.task.delete()
    except CatFactTask.DoesNotExist:
        pass
    
    cat_fact_tasks = CatFactTask.objects.all().order_by('-started')
    return render(request, 'catfactsapp/index.html', {'cat_fact_tasks': cat_fact_tasks})

def breeds(request: HttpRequest) -> HttpResponse:
    response = CatFacts.get_breeds()
    breeds = response['data']
    links = response['links']
    return render(request, 'catfactsapp/breeds.html', {
        'breeds': breeds,
        'links': links
    })

def facts(request: HttpRequest) -> HttpResponse:
    response = CatFacts.get_facts()
    cat_facts = response['data']
    links = response['links']
    return render(request, 'catfactsapp/facts.html', {
        'cat_facts': cat_facts,
        'links': links
    })