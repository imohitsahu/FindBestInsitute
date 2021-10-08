from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
import urllib.request

from findbestclass.models import Student , Institute;

def register(request):
	#return HttpResponse("Registration page");
	return render(request , "findbestclass/register.html" );


def registerInstitute(request):
	for i in request.POST.keys():
		print(i , request.POST[i]);

	admin = request.POST['admin'];
	name = request.POST['name'];
	email = request.POST['email'];
	address = request.POST['address'];
	password = request.POST['password'];
	contact = request.POST['contact'];
	city = request.POST['city'];
	state = request.POST['state'];
	lat = request.POST['lat'];
	lng = request.POST['lng'];
	landmark = request.POST['landmark'];

	institute = Institute(name = name , 
		adminName = admin,
		email = email , 
		password = password , 
		contact = contact,
		address = address, 
		city = city,
		state = state,
		lat = lat , 
		lng = lng , 
		landmark = landmark)

	institute.save();
	return render(request , "findbestclass/login.html")

def registerStudent(request):
	student_error = None;
	if(request.method == "GET"):
		return HttpResponse("<h1>Invalid Url</h1>");

	
	for i in request.POST.keys():
		print(i , request.POST[i]);
	name = request.POST['name']
	email = request.POST['email']
	password = request.POST['password']
	contact = request.POST['contact']
	address = request.POST['address']
	lat = request.POST['lat']
	lng = request.POST['lng']
	city = request.POST['city']
	state= request.POST['state']
	try:
		#Saveing values
		student = Student(name=name , email=email , password=password , contact=contact , address = address , lat = lat , lng = lng , city=city , state = state);
		student.save();

		#login after registration
		student = Student.objects.get(email=email , password=password);
		#saving object to session 
		request.session['studentId'] = student.id;
		del(student._state)
		request.session['student'] = vars(student);
		return render(request , "findbestclass/student/home.html" , {'student' : student});
	except IntegrityError:
		#if email already exists 
		student_error = "Email Already Exists.."
		return render(request , "findbestclass/register.html" , {"student_error":student_error});

	return render(request , "findbestclass/login.html")


def getAddresses(request):
	addr = request.GET['addr'];
	link = "http://www.somesite.com/details.pl?urn=2344"
	url = urllib.request.urlopen("https://apis.mapmyindia.com/advancedmaps/v1/l2dlc7zabjd6wx8ekzjo2ezzvt21i8b3/geo_code?addr="+addr);
	data = url.read();
	print("Addreses : "  , data)
	return HttpResponse(data);

