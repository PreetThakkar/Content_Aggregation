from django.shortcuts import render
from .feeds import *
from .models import *
from django.http import HttpResponse
from . import testdb
from .tasks import *

# Create your views here.
def home(request):
	storee.delay(0)
	return HttpResponse("<h1>Hello</h1")