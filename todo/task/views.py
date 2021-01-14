from django.shortcuts import render,redirect
from .models import *

from .forms import *
# Create your views here.
def todo(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'task/index.html', context)


def update(request,pk):
    #get model
    task = Task.objects.get(id=pk)
    #get form at a certain Model...show example with instance
    form = TaskForm(instance=task)
    #update to Database
    if request.method == 'POST':
        #Update with an instance
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context ={'task':task, 'form':form}
    return render(request, 'task/update.html', context)

def delete(request,pk):
    #get model
    task = Task.objects.get(id=pk)
    
    #update to Database
    if request.method == 'POST':
        #Update with an instance
        task.delete()
        return redirect('/')

    context ={'task':task}
    return render(request, 'task/delete.html', context)