from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.paginator import Paginator


def article_list(request):
	articles = Article.objects.all().order_by('-date')
	paginator = Paginator(articles, 6)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'articles/article_list.html',
		{'page_obj': page_obj})

def article_detail(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', {'article':article})

# Check if user logged in, sent to login page
@login_required(login_url="/accounts/login")
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)# Save but don't commit
			instance.author = request.user # Get and store logged in author
			instance.save()
			return redirect('articles:list')
	else:
		form = forms.CreateArticle()
	return render(request, 'articles/article_create.html', {'form': form})
