from django.urls import path

from .views import CreateTag, CreateTask, UpdateTask, DeleteTask, TaskList, \
     ListTag, index, finish_task, UpdateTag, DeleteTag

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskList.as_view(), name="task-list"),
    path("tasks/create/", CreateTask.as_view(), name="task-create"),
    path("tasks/<int:pk>/update", UpdateTask.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", DeleteTask.as_view(), name="task-delete"),
    path("tags/create/", CreateTag.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", UpdateTag.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", DeleteTag.as_view(), name="tag-delete"),
    path("tags/", ListTag.as_view(), name="tag-list"),
    path("task/<int:pk>/finish", finish_task, name="finish-task"),
]

app_name = "tasks"
