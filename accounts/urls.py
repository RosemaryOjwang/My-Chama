from django.urls import path, include
from accounts import views
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', SignUpView.as_view(), name='login'),
    path('user_admin/', views.user_admin, name='user_admin'),
    path('register_group/', views.register_group, name='register_group'),
    path('add_member/', views.add_member, name='add_member')
 ]