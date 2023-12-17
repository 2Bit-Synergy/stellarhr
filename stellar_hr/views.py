from django.contrib.auth.views import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Extract group names for the logged-in user
        group_names = self.request.user.groups.values_list('name', flat=True)
        context['group_names'] = group_names
        print(group_names)
        return context
