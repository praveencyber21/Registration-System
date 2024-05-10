from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Member
        fields = ('username', 'email', 'password')