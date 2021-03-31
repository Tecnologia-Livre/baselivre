from django.shortcuts import render, get_object_or_404, reverse

from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.models import Group
from groups.forms import CustomGroupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class Index(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups/index.html'
    context_object_name = 'groups' 
    paginate_by = 6

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.all().order_by('name')
        if search:
            object_list = Group.objects.filter(name__icontains=search)
        return object_list


class Create(LoginRequiredMixin, FormView):
    form_class = CustomGroupForm
    template_name = 'groups/create.html'
    success_url = '/groups/'

    def form_valid(self, form):
        group = form.save()
        return super().form_valid(form)


class Update(LoginRequiredMixin, UpdateView):
    form_class = CustomGroupForm
    template_name = 'groups/edit.html'
    success_url = '/groups/'
    model = Group

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class Delete(LoginRequiredMixin, DeleteView):
    template_name = 'groups/delete.html'
    success_url = '/groups/'
    success_message = 'Grupo deletado com sucesso'
    model = Group

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return  self.success_url

