from django.urls import path
from .views import LoginView, RegisterView, custom_logout

app_name = 'apps.account'

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', custom_logout, name="logout"),
]