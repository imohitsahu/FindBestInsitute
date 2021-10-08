from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute;

def studentChangePassword(request):
	print("CHange changeStudentPassowrd")
	cpassword = request.GET['cpassword'];
	npassword = request.GET['npassword'];
	npassword2 = request.GET['npassword2'];
	id = request.session.get('studentId');
	student = Student.objects.get(id=id);
	if(student.password == cpassword):
		student.password = npassword;
		student.save();
		return HttpResponse("ok")
	else:
		return HttpResponse("Current Passowrd is Wrong !! ")
	return HttpResponse("Current Passowrd is Wrong !! ");
	
def isRightOTP(password , otp):
	code = ''
	for i in password:
		uni = ord(i)
		uni = uni * uni
		uni = uni * len(password)
		code = code + str(uni)
		code = str(code);
		code = code[0:5]
	print('code is ' , code)
	print('otp is ' , otp)
	return code == otp

def studentChangePasswordusingOTP(request):
	print("CHange changeStudentPassowrd")
	npassword = request.GET['npassword'];
	otp = request.GET['otp'];
	email = request.session['email']
	print(otp)
	print(email)
	print(npassword)

	try:
		student = Student.objects.get(email=email);
		flag = isRightOTP(student.password , otp )
		print('otp and password matched'  , flag)
		if flag == True:
			student.password = npassword;
			student.save();
			return HttpResponse("true")
		else:
			a = 21/0
	except:
		try:
			print('cheking for institutw')
			institute = Institute.objects.get(email=email)
			print(institute)
			flag = isRightOTP(institute.password , otp)
			print(flag)
			if flag == True:
				institute.password = npassword;
				institute.save();
				return HttpResponse("true")
			else:
				a = 21/0
		except:
			import traceback;
			traceback.print_exc()
			return HttpResponse("Otp Is Incorrect..");

	