from django.urls import path
from .views import todoListView, todoDetailView, todoCreateView, todoDeleteView, todoUpdateView
from django.contrib.auth.decorators import login_required

app_name = "todoApp"

urlpatterns = [
    path("list/", login_required(todoListView.as_view()), name="todoListPage"),
    path("detail/<int:pk>", login_required(todoDetailView.as_view()), name="todoDetailPage"),
    path("create/", login_required(todoCreateView.as_view()), name="todoCreatePage"),
    path("delete/<int:pk>", login_required(todoDeleteView.as_view()), name="todoDeletePage"),
    path("update/<int:pk>", login_required(todoUpdateView.as_view()), name="todoUpdatePage"),
]