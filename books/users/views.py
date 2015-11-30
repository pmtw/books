
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from users.forms import CreateUserForm

# Create your views here.


class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = 'create_form.html'
    success_url = reverse_lazy('user')

class UserList(ListView):
    model = User
    template_name = 'list_users.html'
    
