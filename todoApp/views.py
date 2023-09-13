from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)

# Create your views here.

from .models import TodoModel


class TodoListView(ListView):
    model = TodoModel
    template_name = "home.html"


class TodoCreateView(CreateView):
    model = TodoModel
    context_object_name = "todo"
    template_name = "todo_create.html"
    fields = ["text", "author"]


class TodoDeleteView(DeleteView):
    context_object_name = "todo"
    model = TodoModel
    template_name = "todo_delete.html"
    success_url = reverse_lazy("home")


class TodoUpdateView(UpdateView):
    context_object_name = "todo"
    model = TodoModel
    template_name = "todo_edit.html"
    fields = ["text", "author"]


class TodoDetailView(DetailView):
    context_object_name = "todo"
    model = TodoModel
    template_name = "todo_detail.html"
