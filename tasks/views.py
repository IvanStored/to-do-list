from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task, Tag


def index(request):

    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }

    return render(request, "tasks/index.html", context)


class CreateTask(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class UpdateTask(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class DeleteTask(generic.DeleteView):
    model = Task
    template_name = "tasks/task_сonfirm_delete.html"
    success_url = reverse_lazy("tasks:index")


class TaskList(generic.ListView):
    model = Task
    queryset = model.objects.all()
    template_name = "tasks/task_list.html"


class CreateTag(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class ListTag(generic.ListView):
    model = Tag
    queryset = model.objects.all()
    template_name = "tasks/tag_list.html"


class UpdateTag(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class DeleteTag(generic.DeleteView):
    model = Tag
    template_name = "tasks/tag_сonfirm_delete.html"
    success_url = reverse_lazy("tasks:tag-list")


def finish_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("tasks:task-list")
    )
