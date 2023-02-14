from django.urls import path
from . import views
from .views import OpenAccount

app_name = 'App_bankingSolution'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('AccountOpening/', views.application_view, name="application"),
    ]