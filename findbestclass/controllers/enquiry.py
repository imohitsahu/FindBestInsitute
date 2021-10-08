from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute , Course , Enquiry
import json;
import threading;
from findbestclass.controllers.mail import sendMail;




def save(request):
	courseId = request.GET['courseId'];
	studentId = request.session.get('studentId');
	print('Course Id' , courseId);

	student = Student.objects.get(id=studentId);
	course = Course.objects.get(id = courseId)
	print("Course:   +++++++++ EMail" , course.institute.email)	
	msg = """
		hello , {} 

		You have A new Enquiry for your Course {}
		Studnet information is given bellow 
		
		-----------------------------------------
		Name : {}
		Address : {}
		Contact : {}
		Email : {}

		-----------------------------------------

		For More Information Login At : Http://localhost:8000
	""".format(course.institute.adminName , course.courseName ,  student.name , student.address , student.contact , student.email)
	
	try:
		Enquiry.objects.get(course = course , student = student);
		return HttpResponse("false");
	except:
		enquiry = Enquiry(course = course , student = student , readStatus = 0);
		enquiry.save();
		t = threading.Thread(target = sendMail , args = (msg , course.institute.email))
		t.start()
		return HttpResponse("true");



def getEnquiries(request):
	instituteId = request.session.get('instituteId');
	print("Institute ID : getEnquiries" , instituteId)
	enquries = Enquiry.objects.filter(course__institute_id=instituteId , admissionStatus=0)
	l = list()
	for i in enquries:
		print("1 :" , vars(i))
		print("2 : ", vars(i.student))
		print("3 :  ", vars(i.course))
		print("4 :  ", vars(enquries))
		obj = dict();
		del(i.student._state)
		del(i.course._state)
		
		obj['student'] = (vars(i.student))
		obj['course'] = (vars(i.course)); 
		obj['enquiryId'] = i.id; 
		l.append(obj);
	
	jsonString = json.dumps(l)
	print("======================" , "\n" , jsonString)	
	return HttpResponse(jsonString);


def getAdmitted(request):
	instituteId = request.session.get('instituteId');
	print("Institute ID : getEnquiries" , instituteId)
	enquries = Enquiry.objects.filter(course__institute_id=instituteId , admissionStatus=1)
	l = list()
	for i in enquries:
		print("1 :" , vars(i))
		print("2 : ", vars(i.student))
		print("3 :  ", vars(i.course))
		print("4 :  ", vars(enquries))
		obj = dict();
		del(i.student._state)
		del(i.course._state)
		
		obj['student'] = (vars(i.student))
		obj['course'] = (vars(i.course)); 
		obj['enquiryId'] = i.id; 
		l.append(obj);
	
	jsonString = json.dumps(l)
	print("======================" , "\n" , jsonString)	
	return HttpResponse(jsonString);


def markAdmitted(request):
	print('Mark Admitted')
	try:
		instituteId = request.session.get('instituteId');
		institute = Institute.objects.get(id=instituteId);
		enquiryId = request.GET['id'];
		enquiry = Enquiry.objects.get(id=enquiryId);
		enquiry.admissionStatus = 1;
		enquiry.save();
		
		msg = """
			A new Student " {} " is admitted to Your Institute

			Keep It Up 
			Thannks For Using FBI
		""".format(enquiry.student.name);

		t = threading.Thread(target = sendMail , args = (msg , institute.email))
		t.start()

		#sending mail to studnet
		msg = """
			Hello " {} " , 

			You Are admitted in {} Institute for Course - {}

			Keep It Up 
			Thannks For Using FBI
		""".format(enquiry.student.name , institute.name , enquiry.course.courseName);

		t = threading.Thread(target = sendMail , args = (msg , enquiry.student.email))
		t.start()
		return HttpResponse('true');


	except:
		return HttpResponse('false');

def deleteEnquiry(request):
	print('delete Enquiry')
	try:
		instituteId = request.session.get('instituteId');
		enquiryId = request.GET['id'];
		enquiry = Enquiry(id=enquiryId);
		enquiry.delete();
		return HttpResponse('true');
	except:
		return HttpResponse('false');


	

