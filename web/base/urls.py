from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
	path('', views.homepage),
	path('register/', views.input_form_view, name='input_form'),
	path('about/', views.about),

]

