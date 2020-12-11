from django.http import HttpResponse

def Greetings(request):
	return HttpResponse("Welcome to my weblog, friends!")