from django.shortcuts import render
from django.http import HttpResponse
from . import forms



def input_form_view(request):
	context = {}
	context['form'] = forms.InputForm()
	return render(request, 'register.html', context)

def about(request):
	return render(request, 'about.html')

def homepage(request):
	return render(request, 'homepage.html')
