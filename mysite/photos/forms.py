from django import forms
from .models import transcript

class transcriptForm(forms.ModelForm):
    class Meta:
        model = transcript
        fields = ('url', 'tittle',)