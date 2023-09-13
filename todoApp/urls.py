from django.urls import path


from .views import (
    TodoDeleteView,
    TodoDetailView,
    TodoCreateView,
    TodoListView,
    TodoUpdateView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("new/", TodoCreateView.as_view(), name="todo_new"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("<int:pk>/edit/", TodoUpdateView.as_view(), name="todo_edit"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
]
