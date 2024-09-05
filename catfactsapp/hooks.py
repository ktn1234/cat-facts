from django_q.tasks import Task
from .models import CatFactTask, CatFactStatus

def print_result(task: Task) -> None:
    status = 'Success' if task.success else 'Failed'
    print(f'{task.name} [{task.id}] - {status}')
    
    cat_fact_task = CatFactTask.objects.get(id=task.id)
    cat_fact_task.result = task.result if task.success else None
    cat_fact_task.status = CatFactStatus.SUCCESS.value if task.success else CatFactStatus.FAILED.value
    cat_fact_task.completed = task.stopped
    cat_fact_task.task = task
    cat_fact_task.save()