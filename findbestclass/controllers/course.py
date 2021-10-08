from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute , Course;
import json
from django.db.models import Q
from .rating import getAvgRating , getRatingInfo;


def getAll(request):
	instituteId = request.session.get('instituteId');
	institute = Institute.objects.get(id=instituteId);
	courses = Course.objects.filter(institute = institute);
	lst = list();
	for i in courses:
		dt = vars(i);
		dt.pop('_state')
		lst.append(dt)
	jsonString  = json.dumps(lst) 
	print(jsonString)
	return HttpResponse(jsonString);

def getAllForStudentHome(request):
	courses = Course.objects.all();

	# getting studnet from session object
	studentId = request.session['studentId'];
	student = Student.objects.get(id = studentId);
	
	# cenverting to json
	del(student._state);
	studentjson = vars(student);
	print("student+++++++++++++=== " , studentjson)

	# courses
	lst = list();
	for i in list(courses):
		# Institute.objects.get(i.institute_id)
		# dt.institute.pop('_state')
		print('Vars : ' , vars(i))
		dt = vars(i);
		dt.pop('_state')
		
		institute = vars(Institute.objects.get(id = int(dt['institute_id'])))
		institute.pop('_state')
		dt['institute'] = institute
		dt['avgrate'] = getAvgRating(i);
		dt['ratinginfo'] = getRatingInfo(i);
		lst.append(dt)

	#final respoce String
	resp = dict();
	resp['student'] = studentjson ;
	resp['courses'] = lst
	jsonString  = json.dumps(resp) 
	print(jsonString)
	return HttpResponse(jsonString);


def searchCourse(request):
	#search query 
	q = request.GET['q'];

	#seach resules 
	courses = Course.objects.filter( Q(courseName__contains = q) | Q(institute__name__contains = q) | Q(institute__address__contains = q) |  Q(institute__adminName__contains = q))
	# getting studnet from session object
	studentId = request.session['studentId'];
	student = Student.objects.get(id = studentId);
	
	# cenverting to json
	del(student._state);
	studentjson = vars(student);
	print("student+++++++++++++=== " , studentjson)

	# courses
	lst = list();
	for i in list(courses):
		# Institute.objects.get(i.institute_id)
		# dt.institute.pop('_state')
		print('Vars : ' , vars(i))
		dt = vars(i);
		dt.pop('_state')
		lst.append(dt)
		institute = vars(Institute.objects.get(id = int(dt['institute_id'])))
		institute.pop('_state')
		dt['institute'] = institute
		dt['avgrate'] = getAvgRating(i);
		dt['ratinginfo'] = getRatingInfo(i);


	#final respoce String
	resp = dict();
	resp['student'] = studentjson ;
	resp['courses'] = lst
	jsonString  = json.dumps(resp) 
	print(jsonString)
	return HttpResponse(jsonString);




def save(request):
	name = request.GET['name']
	fees = request.GET['fees']
	print('name : ' , name);
	print('fees : ' , fees);
	instituteId = request.session.get('instituteId');
	institute = Institute.objects.get(id=instituteId);
	course = Course(courseName = name , courseFees = fees , institute = institute);
	course.save();
	asdict = vars(course);
	asdict.pop('_state');
	jsonString  = json.dumps(asdict) 
	print(jsonString)
	return HttpResponse(jsonString);


def delete(request):
	try:
		id = request.GET['id']
		print('id : ' , id);
		course = Course(id = id);
		course.delete();
		return HttpResponse("true");
	except:
		return HttpResponse("false");
