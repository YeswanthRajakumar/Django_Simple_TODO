from django.urls import path, include
from Task import views

urlpatterns = \
    [
        path('home/', views.home, name='home'),
        path('list/', views.task_List, name='task-list'),
        path('create/', views.Create_task, name='task-create'),
        path('update/<int:id>', views.Update_task, name='task-update'),
        path('delete/<int:id>', views.Delete_task, name='task-delete')
    ]
