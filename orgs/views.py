from django.shortcuts import render

from .models import Organisation

def home(request):
	orgs = Organisation.objects.order_by('name')[:5]
	return render(request, 'orgs/home.html', {'orgs':orgs})

def detail(request, id):
	return render(request, 'orgs/detail.html')