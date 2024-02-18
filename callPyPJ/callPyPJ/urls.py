from django.contrib import admin
from django.urls import path, include
from .views import homeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sec/", include("callPyApp.urls")),
    path("", homeView.as_view(), name="homeView"),
]
