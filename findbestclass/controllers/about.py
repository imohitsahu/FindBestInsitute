from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute , Course;
from math import radians, sin, cos, acos
import json;


def about(request):
	return render(request , "findbestclass/about.html");