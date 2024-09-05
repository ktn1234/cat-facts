from django.db import models
from enum import Enum
from django_q.tasks import Task
from django_q.models import OrmQ

# Create your models here.
class CatFactStatus(Enum):
    SUCCESS = 'Success'
    FAILED = 'Failed'
    IN_PROGRESS = 'In Progress'

    @classmethod
    def choices(cls):
        return [(status.value, status.name.replace('_', ' ').title()) for status in cls]

class CatFactTask(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    result = models.TextField(
        default=None,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=CatFactStatus.choices(),
        default=CatFactStatus.IN_PROGRESS.value,
    )
    started = models.DateTimeField(
        null=True,
    )
    completed = models.DateTimeField(
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.OneToOneField(Task, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.task.name} [{self.task.id}] - {self.status}'