# email_verifier/forms.py
from django import forms

class EmailVerifierForm(forms.Form):
    email = forms.EmailField(label='Email Address')
    domain = forms.CharField(label='Domain Name')