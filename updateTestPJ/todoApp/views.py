# todoApp views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import todoTable
from django.urls import reverse_lazy

class todoListView(ListView):
    template_name = "todoList.html"
    model = todoTable

class todoDetailView(DetailView):
    template_name = "todoDetail.html"
    model = todoTable

class todoDeleteView(DeleteView):
    template_name = "todoDelete.html"
    model = todoTable
    success_url = reverse_lazy("todoApp:todoListPage")

class todoCreateView(CreateView):
    template_name = "todoCreate.html"
    model = todoTable
    fields = ("title", "memo", "priority", "deadline")
    success_url = reverse_lazy("todoApp:todoListPage")

class todoUpdateView(UpdateView):
    template_name = "todoUpdate.html"
    model = todoTable
    fields = ("title", "memo", "priority", "deadline")
    def get_success_url(self):
        return reverse_lazy("todoApp:todoDetailPage", kwargs={'pk': self.object.pk})