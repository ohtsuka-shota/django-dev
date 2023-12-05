from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import MyForm

class MyFormView(FormView):
    template_name = "MyForm.html"
    form_class = MyForm
    success_url = reverse_lazy("MyForm:MyFormPage")

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)
