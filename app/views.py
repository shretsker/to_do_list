from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from app.models import Task, Tag

# second try of pull-request issues
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done_or_not = not task.done_or_not  # Перемикаємо статус
    task.save()
    return redirect("app:task-list")  # Переходимо назад на головну сторінку


class TagListView(generic.ListView):
    model = Tag
    template_name = "app/tag_list.html"
    context_object_name = "tags"


class TaskListView(generic.ListView):
    model = Task
    template_name = "app/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tag"]
    template_name = "app/task_add.html"

    def form_valid(self, form):
        # Додаємо нову задачу
        task = form.save(commit=False)
        task.save()
        return redirect("app:task-list")  # Перенаправляємо на головну сторінку


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tag"]
    template_name = "app/task_edit.html"

    def form_valid(self, form):
        # Зберігаємо змінене завдання
        task = form.save(commit=False)
        task.save()
        return redirect("app:task-list")  # Перенаправляємо на головну сторінку


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "app/task_confirm_delete.html"
    success_url = reverse_lazy(
        "app:task-list"
    )  # Після видалення перенаправляємо на головну сторінку


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "app/tag_add.html"

    def form_valid(self, form):
        form.save()
        return redirect("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "app/tag_edit.html"

    def form_valid(self, form):
        form.save()
        return redirect("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "app/tag_confirm_delete.html"
    success_url = reverse_lazy("app:tag-list")
