from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class LogoutView(LoginRequiredMixin, LogoutView):
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        return redirect("apps.account:login")
