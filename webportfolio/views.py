from django.shortcuts import render



def home(request):
	return render(request, 'webportfolio/index.html', {})

def about(request):
	return render(request, 'webportfolio/about.html', {})