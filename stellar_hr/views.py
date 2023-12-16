from django.contrib.auth.views import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login'
