from django.shortcuts import render, redirect
from .models import *
from .tasks import *
import csv
import shutil
import random

# Create your views here.
def redirect_home(request):
	return redirect('home/')

def home(request, source='', cat=''):
	'''
	Fetch feeds from data_new.py
	Rename it to data_old.csv 
	If not then fetch from data.old.csv
	'''
	# data = List of tuples. tuple -> (source, category, title, link)
	dataAll = []
	# sources = dict( { source: list of categories for that source } )
	sources = {}
	try:
		f = open("data_new.csv", 'r', encoding='utf-8')
	except Exception as e:
		f = open("data_old.csv", 'r', encoding='utf-8')
	reader = csv.reader(f)
	name = f.name
	for row in reader:
		dataAll.append(row)
		if row[0] not in sources.keys():
			sources[row[0]] = []
		if row[1] not in sources[row[0]]:
			sources[row[0]].append(row[1])
	if source == '':
		current = random.choice(list(sources.keys()))
	else: current = source
	cats = sources[current]
	data = [row for row in dataAll if row[0] == current]
	f.close()
	if name == "data_new.csv": shutil.move(name, "data_old.csv")
	return render(request, 'sidebar-index.html', context = {'current': current, 'cats': cats, 'data': data, 'sources': sources})
