from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signups.html"
    success_url = reverse_lazy('login')

# Create your views here.
