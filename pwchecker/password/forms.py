from django import forms
from .models import Password

class PasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())
    class Meta:
        model = Password
        fields = '__all__'