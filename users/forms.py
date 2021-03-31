from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Row, Div, Field


class CustomUpdatePasswordForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(CustomUpdatePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'change-password-form'
        self.helper.form_class = 'change-password-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))
        self.helper.layout = Layout(
            Row(
                Div('password1', css_class='col-md-6', ),
                Div('password2', css_class='col-md-6', ),
            ),
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas são diferentes")

        return password2

    class Meta:
        model = User
        fields = ['first_name']


class CustomUserUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'editar-usuario'
        self.helper.form_class = 'editar-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))
        self.helper.layout = Layout(
            Row(
                Div('username', css_class='col-md-4', ),
                Div('first_name', css_class='col-md-4', ),
                Div('last_name', css_class='col-md-4', ),
            ),
            Row(
                Div('email', css_class='col-md-4', ),
                Div(Field('date_joined', readonly=True), css_class='col-md-4', ),
                Div(Field('last_login', readonly=True), css_class='col-md-4', ),
            ),
            Row(
                Div(Field('groups', css_class='selectpicker'), css_class='col-md-6', ),
                Div(Field('user_permissions', css_class='selectpicker'), css_class='col-md-6', ),
            ),
            Div('is_superuser', css_class='col-md-4', ),
            Div('is_staff', css_class='col-md-4', ),
            Div('is_active', css_class='col-md-4', ),
        )

    class Meta:
        model = User
        exclude = [
            'password'
        ]


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'cadastro-usuario'
        self.helper.form_class = 'cadastro-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))
        self.helper.layout = Layout(
            Row(
                Div('username', css_class='col-md-4', ),
                Div('first_name', css_class='col-md-4', ),
                Div('last_name', css_class='col-md-4',),
            ),
            Row(
                Div('email', css_class='col-md-4', ),
                Div('password1', css_class='col-md-4', ),
                Div('password2', css_class='col-md-4', ),
            ),
            Row(
                Div(Field('groups', css_class='selectpicker'), css_class='col-md-6', ),
                Div(Field('user_permissions', css_class='selectpicker'), css_class='col-md-6', ),
            ),
            Div('is_superuser', css_class='col-md-4', ),
            Div('is_staff', css_class='col-md-4', ),
            Div('is_active', css_class='col-md-4', ),
        )


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count() and email != "":
            raise  ValidationError("E-mail já cadastrado")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas são diferentes")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password2'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            is_superuser=self.cleaned_data['is_superuser'],
            is_staff=self.cleaned_data['is_staff'],
            is_active=self.cleaned_data['is_active'],
        )
        return user

    class Meta:
        model = User
        exclude = [
            'date_joined', 'password'
        ]

