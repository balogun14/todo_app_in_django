from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

from .models import TodoModel


class TodoListView(LoginRequiredMixin,ListView):
    model = TodoModel
    template_name = "home.html"


class TodoCreateView(LoginRequiredMixin,CreateView):
    model = TodoModel
    context_object_name = "todo"
    template_name = "todo_create.html"
    fields = ["text"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    context_object_name = "todo"
    model = TodoModel
    template_name = "todo_delete.html"
    success_url = reverse_lazy("home")
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TodoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    context_object_name = "todo"
    model = TodoModel
    template_name = "todo_edit.html"
    fields = ["text"]

    def test_func(self):
        """
        docstring
        """
        obj = self.get_object()
        return obj.author == self.request.user


class TodoDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "todo"
    model = TodoModel
    template_name = "todo_detail.html"
