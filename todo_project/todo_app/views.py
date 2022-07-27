from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from .forms import TaskForm
# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_detail.html'

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create.html'
    # fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update.html'
    # fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('task-list')
