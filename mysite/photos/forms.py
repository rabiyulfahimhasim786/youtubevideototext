from django import forms
from .models import transcript, generate_transcript

class transcriptForm(forms.ModelForm):
    class Meta:
        model = transcript
        fields = ('url', 'tittle',)

class generate_transcriptForm(forms.ModelForm):
    class Meta:
        model = generate_transcript
        fields = ('urlid', 'title',)