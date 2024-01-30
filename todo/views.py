from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def index(request):
    complete_task = Todo.objects.filter(completed=True)
    incomplete_task = Todo.objects.filter(completed=False)

    context = {
        'complete_task': complete_task,
        'incomplete_task': incomplete_task
    }
    return render(request, 'index.html', context)


def addTask(request):
    task = request.POST['task']
    Todo.objects.create(task=task)
    return redirect('index')


def mark_as_done(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.completed = True
    task.save()
    return redirect('index')


def mark_as_undone(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.completed = False
    task.save()
    return redirect('index')


def edit_task(request, pk):
    get_task = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('index')
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)


def delete_task(request, pk):
    get_task = get_object_or_404(Todo, pk=pk)
    get_task.delete()
    return redirect('index')
