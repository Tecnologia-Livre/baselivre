from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, RedirectView, View
from django.contrib.auth import login, logout as auth_logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib import messages
from django.conf import settings

class Login(View):
    def get(self, request):
        return render(request, 'core/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                messages.add_message(request, messages.WARNING, 'Usuário Inativo')
                return HttpResponseRedirect(settings.LOGIN_URL)
        else:
            messages.add_message(request, messages.ERROR, 'E-mail ou senha inválidos.')
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")


class Logout(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(Logout, self).get(request, *args, **kwargs)


class ForgotPassword(View):
    def get(self, request):
        return render(request, 'core/form_email_trocar_senha.html')

    def post(self, request):
        email = request.POST['email']
        if email:
            form = PasswordResetForm({'email': email})
            if form.is_valid():
                form.save()
                return render(request, 'core/email_trocar_senha_sucesso.html')
            else:
                return render(request, 'core/email_trocar_senha_erro.html')
        else:
            messages.info(request, 'Informe um e-mail')
            return render(request, 'core/form_email_trocar_senha.html')


class Home(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"


class Register(FormView):
    template_name = "core/register.html"
    form_class = UserCreationForm
    success_url = "/home/"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)