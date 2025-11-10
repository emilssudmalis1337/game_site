# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Import the form we just created
from .forms import SignUpForm


class SignUpView(CreateView):
    """
    Renders the signup template and creates a new CustomUser.
    After a successful sign‑up the user is redirected to the login page.
    """
    form_class = SignUpForm               # <-- use our custom form
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"