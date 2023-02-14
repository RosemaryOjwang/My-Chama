from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
#from django.contrib.auth.views import LoginView
#from django.urls import reverse


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
#class SignUpView(LoginView):
#   def form_valid(self, form):
#        self.success_url_kwargs = {'username': form.clean_data['username']}
#        return super().form_valid(form)

#    def get_success_url(self):
#       return reverse('App_bankingSolution:application')

