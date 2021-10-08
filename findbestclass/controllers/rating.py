from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute , Course , Rating;
import json
from django.db.models import Avg;


def rate(request):
	studentId = request.session.get('studentId' , 0);
	if(studentId == 0):
		return HttpResponse("Login Please");

	student = Student.objects.get(id = studentId)
	courseId = request.GET['id'];
	rate  = request.GET['rate']
	course = Course.objects.get(id=courseId)

	try:
		rating = Rating.objects.get(student = student , course = course);
		print(rating)
		rating.rate = rate;
		rating.save();
	except:
		print('Exception...............')
		rating = Rating(student = student , course = course , rate = rate);
		rating.save();
	return HttpResponse(True);

def getAvgRating(course):
	rate = Rating.objects.filter(course = course).aggregate(Avg('rate'));
	if(rate['rate__avg'] == None):
		return 0
	return round(rate['rate__avg']);


def getRatingInfo(course):
	avgrate = Rating.objects.filter(course = course).aggregate(Avg('rate'));
	one = len(Rating.objects.filter(course = course , rate = 1))
	two = len(Rating.objects.filter(course = course , rate = 2))
	three = len(Rating.objects.filter(course = course , rate = 3))
	four = len(Rating.objects.filter(course = course , rate = 4))
	five = len(Rating.objects.filter(course = course , rate = 5))
	total = one + two + three + four + five ;
	avg = 0.0;
	print("1" , one)
	if(avgrate['rate__avg'] == None):
		avg = 0.0
	avg = avgrate['rate__avg'];

	di = dict();
	di['avg'] = str(avg)[:3];
	di['total'] = total;
	di['one'] = one;
	di['two'] = two;
	di['three'] = three;
	di['four'] = four;
	di['five'] = five;

	return di;



	

