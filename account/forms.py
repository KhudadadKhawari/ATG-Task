from django.forms import ModelForm
from .models import User, Address
from django import forms


class UserForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'profile_picture', 'user_type']
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        return username


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['line1', 'city', 'state', 'pincode']

