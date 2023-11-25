from django.contrib import admin
from django.urls import path
from .views import homeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView.as_view(), name="home"),
]