from django import forms
from .models import Field, FieldData


class FieldForm(forms.Form):
    data = forms.CharField(max_length=255)


class FieldDataForm(forms.ModelForm):
    class Meta:
        model = FieldData
        fields = ['data']
