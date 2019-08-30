from django import forms
from .models import Blog

class UserRegistrationForm(forms.Form):
	username = forms.CharField(
		required = True,
		label = 'Username',
		max_length = 32
	)
	email = forms.CharField(
		required = True,
		label = 'Email',
		max_length = 32,
	)
	password = forms.CharField(
		required = True,
		label = 'Passowrd',
		max_length = 32,
		widget = forms.PasswordInput()
	)

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'body']
