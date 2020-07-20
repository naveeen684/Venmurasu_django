from django import forms
from .models import Word
from django.conf import settings


class CharForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['word']


class IntForm(forms.ModelForm):
    length = forms.IntegerField(required=False, min_value=0)

    class Meta:
        model = Word
        fields = ['length']
