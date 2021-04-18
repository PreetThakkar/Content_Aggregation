from django.shortcuts import render
from .feeds import *
from .models import *
from django.http import HttpResponse
# from . import testdb
from .tasks import *

# Create your views here.
def home(request):
	# fetch feeds from data_new.py. if not then fetch from data.old.csv and then rename it to data_old.csv
	storee.delay(0)
	return HttpResponse("<h1>Hello</h1")