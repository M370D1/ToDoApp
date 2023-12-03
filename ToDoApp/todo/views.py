from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ToDoApp.todo.forms import ItemAddForm
from ToDoApp.todo.models import ToDoItem


# Create your views here.
@login_required
def todo_add(request):
    form = ItemAddForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        # form.save()

        return redirect('todo-add')

    user_todo_items = ToDoItem.objects.all()

    context = {
        'form': form,
        'user_todo_items': user_todo_items,
    }

    return render(request, template_name='todo-add-page.html', context=context)


@login_required
def todo_delete(request, todo_id):
    ToDoItem.objects.get(id=todo_id).delete()

    return redirect('todo-add')
