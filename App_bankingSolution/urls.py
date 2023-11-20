from django.urls import path
from . import views
from .views import OpenAccount

app_name = 'App_bankingSolution'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('AccountOpening/', views.application_view, name="application"),
    path('user_admin/', views.user_admin, name='user_admin'),
    path('edit_member/', views.edit_member, name='edit_member')    
    ]