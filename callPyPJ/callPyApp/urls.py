# callPyApp/urls.py
from django.urls import path
from .views import encryptView, decryptView

app_name = "callPyApp"

urlpatterns = [
    path("encrypt/", encryptView.as_view(), name="encryptView"),
    path("decrypt/", decryptView.as_view(), name="decryptView"),
]