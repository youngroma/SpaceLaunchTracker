from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserRegisterForm


class LoginView(LoginView):
    template_name = 'launch_tracker/login.html'


class LogoutView(LogoutView):
    next_page = 'index'

class RegisterView(FormView):
    template_name = 'launch_tracker/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)