from django.shortcuts import render, redirect
from .models import ToDo 
from .forms import ToDoForm
from django.contrib import messages

# Create your views here.

def home(request):
    all_items = ToDo.objects.all

    if request.method == "POST":
        form = ToDoForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'home.html', {'all_items':all_items} )

    else:
        form = ToDoForm()
        return render(request, 'home.html', {'all_items':all_items} )


def delete(request, task_id):
    item = ToDo.objects.get(id=task_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')
    

def cross_off(request, task_id):
    item = ToDo.objects.get(id=task_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, task_id):
    item = ToDo.objects.get(id=task_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, task_id):
    if request.method == "POST":
        item = ToDo.objects.get(id=task_id)

        form = ToDoForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')

    else:
        item = ToDo.objects.get(id=task_id)
        return render(request, 'edit.html', {'item' : item})