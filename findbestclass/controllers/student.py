from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute ,Rating, Enquiry;
import json;

def studentProfile(request):
	student = request.session['student'];
	return render(request , "findbestclass/student/student_profile.html" , {'student' : student});


def getCoursesOfStudent(request):
	student = request.session['student'];
	enquiries = Enquiry.objects.filter(student=student['id'] , admissionStatus=1);
	l = list();
	for i in enquiries:
		course = i.course;
		Institute = course.institute;
		del(course._state)
		del(Institute._state)
		del(i._state);
		d = dict();
		d['course'] = vars(course);
		try:
			rate = Rating.objects.get(student = student['id'] , course = course );
			d['rating'] = rate.rate;
		except:
			d['rating'] = 0
		print(d['rating'] , course.id , student['id'] );
		d['institute'] = vars(Institute);
		l.append(d)

	return HttpResponse(json.dumps(l))


def searchCourse(request):
	student = request.session['student'];
	enquiries = Enquiry.objects.filter(student=student['id'] , admissionStatus=1);
	l = list();
	for i in enquiries:
		course = i.course;
		Institute = course.institute;
		del(course._state)
		del(Institute._state)
		del(i._state);
		d = dict();
		d['course'] = vars(course);
		try:
			rate = Rating.objects.get(student = student['id'] , course = course );
			d['rating'] = rate.rate;
		except:
			d['rating'] = 0
		print(d['rating'] , course.id , student['id'] );
		d['institute'] = vars(Institute);
		l.append(d)

	return HttpResponse(json.dumps(l))