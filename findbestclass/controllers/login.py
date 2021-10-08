from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute;

def login(request):
	if request.method == "POST":
		email = request.POST['email'];
		password = request.POST['password'];

		print('---------------------------------------------------')
		print("Email : " ,email );
		print("Password : " , password);
		print('---------------------------------------------------')
		try:
			students = Student.objects.get(email=email , password=password);
			#saving object to session 
			request.session['studentId'] = students.id;
			del(students._state)
			request.session['student'] = vars(students);
			# print("=======" , request.session['student'])
			# return render(request , "findbestclass/student/student_profile.html" , {'student' : students});
			return render(request , "findbestclass/student/home.html" , {'student' : students , 'showSearchBar':True});
		except ObjectDoesNotExist:
			#if student login failed then try to login with institute
			try:
				institute = Institute.objects.get(email=email , password=password);
				#saving object to session 
				request.session['instituteId'] = institute.id;
				return render(request , "findbestclass/institute/homepage.html" , {'institute' : institute});
			except ObjectDoesNotExist:
				return render(request , "findbestclass/login.html" , {'error' : "email or password incorrect !! "})
	else:	
		return 


