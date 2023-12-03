from django.urls import path

from ToDoApp.todo.views import todo_add, todo_delete

urlpatterns = [
    path('todo_add/', todo_add, name='todo-add'),
    path('todo_delete/<int:todo_id>/', todo_delete, name='todo-delete'),
]