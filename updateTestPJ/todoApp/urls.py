from django.urls import path
from .views import todoListView, todoDetailView, todoCreateView, todoDeleteView

app_name = "todoApp"

urlpatterns = [
    path("list/", todoListView.as_view(), name="todoListPage"),
    path("detail/<int:pk>", todoDetailView.as_view(), name="todoDetailPage"),
    path("create/", todoCreateView.as_view(), name="todoCreatePage"),
    path("delete/<int:pk>", todoDeleteView.as_view(), name="todoDeletePage"),
]