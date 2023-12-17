from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import LoginForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('apps.account:login')
    template_name = 'register.html'

class LoginView(DjangoLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = reverse_lazy('main')
    success_url = reverse_lazy('main')
    form_class = LoginForm

def custom_logout(request):
    logout(request)
    # Redirect to the desired URL after logout
    return redirect('/login')