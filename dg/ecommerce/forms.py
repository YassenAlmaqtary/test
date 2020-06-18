from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text=' first Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password1', 'password2',)




class UserForm(forms.ModelForm):
      first_name = forms.CharField(max_length=100, help_text=' first Name')
      last_name = forms.CharField(max_length=100, help_text='Last Name')
      email = forms.EmailField(max_length=150, help_text='Email')
      class Meta:
          model=User
          fields = ( 'first_name', 'last_name','email',)


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(max_length=100, help_text='image')
    country =CountryField()
    address = forms.CharField(max_length=150, help_text='address')
    slug=forms.CharField(max_length=100,help_text='slug')
    bio=forms.Textarea()
    class Meta:
        model=Profile
        fields=('image','country','address','slug','bio')
