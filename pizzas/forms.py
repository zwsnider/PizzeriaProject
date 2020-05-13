from django import forms

from .models import Pizza

class CommentForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}
        widgets = {'name': forms.Textarea(attrs={'cols': 50})}