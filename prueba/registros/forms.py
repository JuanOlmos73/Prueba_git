from django import forms
from django.db.models import fields
from .models import ComentarioContacto


class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario','mensaje']