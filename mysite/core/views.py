from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, BlogForm
from .models import Blog

def index_page(request):
	blogs = Blog.objects.all()
	return render(request, 'mysite/index_page.html', {'blogs': blogs})

def show_item(request, id):
	 blog = Blog.objects.get(id=id)

	 return render(request, 'mysite/item_page.html', {'blog': blog})

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email = userObj['email']
			password = userObj['password']
			if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				User.objects.create_user(username, email, password)
				user = authenticate(username = username, password = password)
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				raise forms.ValidationError('Looks like a username with that email or password already exists!')
	else:
		form = UserRegistrationForm()
	return render(request, 'mysite/register.html', {'form': form})

def create_blog(request):
	form = BlogForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('index_page')

	return render(request, 'mysite/blog-form.html', {'form': form})

def update_blog(request, id):
	blog = Blog.objects.get(id=id)
	form = BlogForm(request.POST or None, instance=blog)

	if form.is_valid():
		form.save()
		return redirect('index_page')

	return render(request, 'mysite/blog-form.html', {'form': form, 'blog':blog})


def delete_blog(request, id):
	blog = Blog.objects.get(id=id)

	if request.method == 'POST':
		blog.delete()
		return redirect('index_page')

	return render(request, 'mysite/blog-delete.html', {'blog': blog})

