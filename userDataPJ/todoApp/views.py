# todoApp/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import todoTable
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class todoListView(ListView):
    template_name = "todoList.html"
    model = todoTable
    context_object_name = 'user_todos'  

    def get_queryset(self):  
        return todoTable.objects.filter(user=self.request.user)

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("todoApp:todoListPage")

class todoUpdateView(UpdateView):
    template_name = "todoUpdate.html"
    model = todoTable
    fields = ("title", "memo", "priority", "deadline")

    def get_success_url(self):
        return reverse_lazy("todoApp:todoDetailPage", kwargs={'pk': self.object.pk})
