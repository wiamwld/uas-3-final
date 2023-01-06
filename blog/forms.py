from django.forms import ModelForm
from django import forms
from .models import blog


class ContactForm(ModelForm):
    class Meta:
        model = blog
        fields = '__all__'

        widgets = {
            'Nama': forms.TextInput({'class': 'form-control'}),
            'Email': forms.TextInput({'class': 'form-control'}),
            'Pesan': forms.TextInput({'class': 'form-control'}),
        }
