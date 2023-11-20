#from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
#from django.urls import reverse_lazy
#from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View



# Create your views here.
@login_required
def edit_member(request):
    return render(request, 'user_admin.html')
