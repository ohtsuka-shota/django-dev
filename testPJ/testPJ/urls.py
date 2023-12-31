# This is Project urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import homeView, UserCreateView

index_view = TemplateView.as_view(template_name="index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", login_required(index_view), name="index"),
    path("polls/", include("polls.urls")),
    path("auth/", include("django.contrib.auth.urls"), name="login"),
    path("createuser/", UserCreateView.as_view(), name="userCreate"),
    path('', homeView.as_view(), name="home"),
]
