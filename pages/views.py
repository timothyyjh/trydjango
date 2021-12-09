from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	my_context = {
		"my_text" : "bond",
		"my_number" : 69420,
		"my_list" : [1,2,3,'a']
	}
	return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Hi</h1>")