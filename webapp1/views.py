from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
import MySQLdb

def index(request):
	return render(request, 'index.html')



   