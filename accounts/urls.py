from django.urls import path
from . import views

urlpatterns = [
    # /register
    path('register/', views.register, name='accounts-register'),
    # /login
]