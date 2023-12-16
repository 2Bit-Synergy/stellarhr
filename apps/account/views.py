from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import LoginForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'register.html'

class LoginView(DjangoLoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy("main")

class LogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        return redirect("account:login")
