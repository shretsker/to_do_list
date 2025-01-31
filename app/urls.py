from django.urls import path

from app.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    complete_task,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/add/", TaskCreateView.as_view(), name="task-add"),
    path("task/<int:pk>/update/",
         TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/",
         TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/complete/", complete_task, name="task-complete"),
    path("tags/add/", TagCreateView.as_view(), name="tag-add"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

# noinspection PyUnresolvedReferences
app_name = "app"
