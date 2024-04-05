# email_verifier/urls.py
from django.urls import path
from . import views

app_name = 'email_verifier'
urlpatterns = [
    path('', views.verify, name='verify'),
]