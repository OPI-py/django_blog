from django.shortcuts import render
from .forms import InputForm

def input_form_view(request):
	context = []
	context['form'] = InputForm()
	return render(request, 'home.html', context)
