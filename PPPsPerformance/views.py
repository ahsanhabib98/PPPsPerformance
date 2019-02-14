from django.shortcuts import render

# Create your views here.



def home(request):
	template = 'home.html'
	return render(request, template)


def phase(request):
	template = 'phase.html'
	return render(request, template)

