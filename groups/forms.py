from django.contrib.auth.models import Group
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Row, Div, Field

class CustomGroupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomGroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'group-form'
        self.helper.form_class = 'group-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))
        self.helper.layout = Layout(
            Row(
                Div('name', css_class='col-md-6', ),
                Div( Field('permissions', css_class='selectpicker', ), css_class='col-md-6',) ,
            ),
        )

    class Meta:
        model = Group
        fields = ['name', 'permissions']