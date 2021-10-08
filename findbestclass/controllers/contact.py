from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute , Course;
from math import radians, sin, cos, acos
import json;
from django.views import View



class Contact(View):
	def get(self , request):
		print('class based')
		return render(request , "findbestclass/contact.html");