from django.urls import path
from base import views

urlpatterns = [
	path('register/', views.input_form_view, name='input_form')

]

