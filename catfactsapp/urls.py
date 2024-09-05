from django.urls import path
from .views import index, facts, breeds, index_delete

urlpatterns = [
    path('', index, name='index'),
    path('index_delete/<str:task_id>', index_delete, name='index_delete'),
    path('facts', facts, name='facts'),
    path('breeds', breeds, name='breeds'),
]