from django import forms

from Departamentos.models import Depto


class DeptoForm(forms.ModelForm):
    titdepto = forms.CharField(max_length=255)
    direccion = forms.CharField(max_length=255)

    class Meta:
        model = Depto
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg
