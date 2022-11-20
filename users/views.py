from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView

from users.forms import UserCreateForm


class LoginInterfaceView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = 'You are logged in'


class LogoutInterfaceView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'You are logged out')
        return response


class SignupView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_message = 'You are successfully signed up'

    def get_success_url(self):
        return reverse('login')
