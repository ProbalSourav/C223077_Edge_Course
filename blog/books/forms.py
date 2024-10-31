from django import forms
from typing import Any

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        email = self.cleaned_data.get('email')
        
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email should end with @example.com')
        return email
 
   