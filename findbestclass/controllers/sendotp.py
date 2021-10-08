from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute;
import traceback


from findbestclass.controllers import mail;


def sendOtp(request):
	print("Sending OTp.....")
	email = request.GET['email'];
	request.session['email'] = email ;
	try:
		student = Student.objects.get(email=email);
		otp = passwordOTP(student.password)
		print(otp  , '---------------')
		print(student.email.strip())
		mail.sendMail( message = "Hello " + student.name + "Your password Reset OTP is "+otp, to = student.email.strip())
		print('sent')
	except:
		try:
			institute = Institute.objects.get(email=email);
			otp = passwordOTP(institute.password)
			mail.sendMail( "Hello , "+ institute.name +" Your password Reset OTP Is" + otp , institute.email.strip())
			print(otp)
		except:
			traceback.print_exc()
			return HttpResponse("false");
	return HttpResponse("OTP Sent To Your Email");
	
	
	

def passwordOTP(password):
	code = ''
	for i in password:
		uni = ord(i)
		uni = uni * uni
		uni = uni * len(password)
		code = code + str(uni)
		code = str(code);
		code = code[0:5]
	return str(code)
