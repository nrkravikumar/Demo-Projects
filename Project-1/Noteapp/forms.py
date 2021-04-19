from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Noteapp.models import ImProfile
from django.utils.translation import gettext_lazy as _

class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Username",
			}),
		}
		


class UtupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name",
			}),
		}

class ImForm(forms.ModelForm):
	class Meta:
		model = ImProfile
		fields = ["age","gender","impf"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select Your Gender",
			}),
		}

class ChpasForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"New password Confirmation"}))
	class Meta:
		model = User