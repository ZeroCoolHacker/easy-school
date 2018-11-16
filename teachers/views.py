# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from forms.forms import UserCreateForm


class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
