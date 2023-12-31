from django.contrib import admin
from django.urls import path, include
from .views import homeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("django.contrib.auth.urls"), name="login"),
    path("todo/", include("todoApp.urls")),
    path("", homeView.as_view(), name="homePage"),
]