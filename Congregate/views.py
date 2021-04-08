from django.shortcuts import render
from .feeds import *
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
	print("Home")

def store(request):
	objects = [bbc.BBC(), engadget.Engadget(), medium.Medium(), byteiota.Byteiota()]
	for object in objects:
		for results in object.getAll():
			for result in results:
				mod = Content_Model()
				mod.source = result[0]
				mod.category = result[1]
				mod.title = result[2]
				mod.url = result[3]
				mod.save()
	return HttpResponse('<h1>Success Storage of Content</h1>')