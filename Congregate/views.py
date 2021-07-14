from django.shortcuts import render, redirect
from .feeds import *
from .models import *
from django.http import HttpResponse
from .tasks import *
import csv
from collections import defaultdict
import shutil

# Create your views here.
def redirect_home(request):
	return redirect('home/')

def home(request, source='', cat=''):
	'''
	Fetch feeds from data_new.py
	Rename it to data_old.csv 
	If not then fetch from data.old.csv
	'''
	data = []
	sources = {}
	cat_count = defaultdict(int)
	try:
		f = open("data_new.csv", 'r', encoding='utf-8')
	except Exception as e:
		f = open("data_old.csv", 'r', encoding='utf-8')
	reader = csv.reader(f)
	for row in reader:
		current = " - ".join([row[0], row[1]])
		if source:
			if row[0] == source:
				data.append(row)
				if row[0] not in sources.keys():
					sources[row[0]] = []
				if row[1] not in sources[row[0]]:
					sources[row[0]].append(row[1])
		else:
			if cat_count[current] == 0:
				if row[0] not in sources.keys():
					sources[row[0]] = []
				if row[1] not in sources[row[0]]:
					sources[row[0]].append(row[1])
			if cat_count[current] < 5:
				data.append(row)
				cat_count[current] += 1
	name = f.name
	f.close()
	if name == "data_new.csv":
		shutil.move(name, "data_old.csv")
	if source:
		return render(request, 'index.html', context = {'data': data, 'sources': sources, 'rang': range(5)})
	else:
		return render(request, 'flex-index.html', context = {'data': data, 'sources': sources, 'rang': range(5)})