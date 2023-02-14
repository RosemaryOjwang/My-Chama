from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', SignUpView.as_view(), name='login')
 ]