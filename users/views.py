from django.shortcuts import render, get_object_or_404, reverse

from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.models import User
from users.forms import CustomUserCreationForm, CustomUserUpdateForm
from users.forms import CustomUpdatePasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class Index(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users' 
    paginate_by = 6

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.all().order_by('username')
        if search:
            object_list = User.objects.filter(username__icontains=search)
        return object_list

class Create(LoginRequiredMixin, FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/create.html'
    success_url = '/users/'

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class Update(LoginRequiredMixin, UpdateView):
    form_class = CustomUserUpdateForm
    template_name = 'users/edit.html'
    success_url = '/users/'
    model = User

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class UpdatePassword(LoginRequiredMixin, UpdateView):
    form_class = CustomUpdatePasswordForm
    template_name = 'users/password/edit.html'
    success_url = '/users/'
    model = User

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password2'])
        self.object.save()
        return super().form_valid(form)


class Delete(LoginRequiredMixin, DeleteView):
    template_name = 'users/delete.html'
    success_url = '/users/'
    success_message = 'Usuário deletado com sucesso'
    model = User

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return  self.success_url

