from django import forms
from django.forms import ModelForm

from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields= '__all__'

class UserRegister(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Enter Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password1', 'password2')

class UpdateCustomer(ModelForm):
    name = forms.CharField(label='Enter Name', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Enter Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(label='Enter Phone number', widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Customer
        fields =('name', 'phone', 'email', 'pic')
        exclude = ['user']