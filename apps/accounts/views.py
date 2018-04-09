from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
)

from accounts.forms import UserRegisterForm
from accounts.mixins import OwnerRequiredMixin

User = get_user_model()

class UserCreateView(CreateView):
    template_name = 'accounts/registration/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        valid = super(UserCreateView, self).form_valid(form)
        username = self.request.POST.get("username").strip()
        password = self.request.POST.get("password")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid

    def get_success_url(self):
        return self.object.get_absolute_url()

class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

class UserUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/user_update.html'
    fields = [
        'image',
        'first_name',
        'last_name',
        'email',
        'gender',
    ]

    def get_object(self, *args, **kwargs):
        username = self.kwargs.get('username')
        print(username)
        instance = get_object_or_404(User, username=username)
        return instance

class UserDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = '/'

    def get_object(self, *args, **kwargs):
        username = self.kwargs.get('username')
        instance = get_object_or_404(User, username=username)
        return instance
