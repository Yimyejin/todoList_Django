from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TodoList
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    todos = TodoList.objects.all()
    return render(request, 'home.html', {'todos':todos})

def plus(request,id):
    todo = get_object_or_404(TodoList, pk=id)
    return render(request, 'plus.html',{'todo':todo})

def create(request):
    new_todo = TodoList()
    new_todo.content = request.POST['content']
    new_todo.plusmemo = request.POST['plusmemo']
    new_todo.date = timezone.now()
    new_todo.save()
    return redirect('home')

def delete(request,id):
    delete_todo=TodoList.objects.get(id=id)
    delete_todo.delete()
    return redirect('home')

def edit(request,id):
    edit_todo = TodoList.objects.get(id=id)
    return render(request,'edit.html',{'todo':edit_todo})

def update(request,id):
    update_todo = TodoList.objects.get(id=id)
    update_todo.content = request.POST['content']
    update_todo.plusmemo = request.POST['plusmemo']
    update_todo.date = timezone.now()
    update_todo.save()
    return redirect('home')

