from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(max_length=15, required=False, help_text='Optional. Enter your phone number.')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_phone_no(self):
        phone_no = self.cleaned_data['phone_no']
        if UserProfile.objects.filter(phone_no=phone_no).exists():
            raise forms.ValidationError("Phone number already in use.")
        return phone_no