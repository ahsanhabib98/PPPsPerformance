from django.shortcuts import render
from .models import PhaseCategory, PhaseSubCategory

# Create your views here.



def category(request):
	category = PhaseCategory.objects.all()
	context = {
		'category': category
	}
	template = 'phase/category.html'
	return render(request, template, context)

def sub_category(request, id):
	subcategory = PhaseSubCategory.objects.filter(category__id=id)
	context = {
		'subcategory': subcategory,
	}
	template = 'phase/subcategory.html'
	return render(request, template, context)

def child_category(request, id):
	childcategory = PhaseSubCategory.objects.get(id=id)
	childcategory = childcategory.child
	context = {
		'childcategory': childcategory
	}
	template = 'phase/childcategory.html'
	return render(request, template, context)

