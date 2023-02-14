#from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
#from django.urls import reverse_lazy
#from django.views import generic
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class OpenAccount(View):
    def get(self, request, username):
        return HttpResponse('Hello' + username + '!')
