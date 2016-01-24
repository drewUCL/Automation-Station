from django.shortcuts import render

# Create your views here.

#need to pass request 
def index(request): 
	return render(request, 'personal/home.html') #must pass render, then the location of the HTML template you want to render. WITH JINJA CAN ALSO PASS A DICTIONARY TO THE HTML FILE FULL OF DATA
