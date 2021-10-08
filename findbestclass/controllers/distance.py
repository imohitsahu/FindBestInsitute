from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute , Course;
from math import radians, sin, cos, acos
import json;

def calculateDistance(request):

	
	print("Input coordinates of two points:")
	slat = request.GET['lat1']
	slon = request.GET['lng1']
	elat = request.GET['lat2']
	elon = request.GET['lng2']

	dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
	print("The distance is %.2fkm." % dist)
	return HttpResponse(str(dist))

