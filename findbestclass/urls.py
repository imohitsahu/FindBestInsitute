
from django.urls import path
from . import views;
from .controllers import login , registration 
from .controllers import  changePassword , course , distance 
from .controllers import enquiry , logout , student , rating , about , sendotp; 
from .controllers.contact import Contact; 


urlpatterns = [
    path('', views.showLoginPage , name='showLoginPage') ,  
    path('login', login.login  , name='login') ,
    path('logout/', logout.logout  , name='logout') ,
    path('registration', registration.register  , name='register') ,
    path('student_registration' , registration.registerStudent , name='registerStudent') , 
    path('institute_registration' ,  registration.registerInstitute , name='registerInstitute') , 
    path('student_change_password/' ,  changePassword.studentChangePassword , name='studentChangePassword') , 
    path('change_password_otp/' ,  changePassword.studentChangePasswordusingOTP , name='studentChangePasswordusingOTP') , 
    path('get_addresses/' ,  registration.getAddresses , name='getAddresses') , 
    path('save_course/' ,  course.save , name='save') , 
    path('get_all_courses/' ,  course.getAll , name='getAll') ,
    path('courses_student_home/' ,  course.getAllForStudentHome , name='getAllForStudentHome') , 
    path('delete_course/' ,  course.delete , name='delete') , 
    path('clc_distance/' ,  distance.calculateDistance , name='calculateDistance') , 
    path('save_enquiry/' ,  enquiry.save , name='save') , 
    path('get_enquiries/' ,  enquiry.getEnquiries , name='getEnquiries') , 
    path('get_admitted/' ,  enquiry.getAdmitted , name='getAdmitted') , 
    path('mark_admitted/' ,  enquiry.markAdmitted , name='markAdmitted') , 
    path('delete_enquiry/' ,  enquiry.deleteEnquiry , name='deleteEnquiry') , 
    path('student_profile/' ,  student.studentProfile , name='studentProfile') , 
    path('student_courses/' ,  student.getCoursesOfStudent , name='getCoursesOfStudent') , 
    path('rate/' ,  rating.rate , name='rate') , 
    path('search/' ,  course.searchCourse , name='searchCourse') , 
    path('about/' ,  about.about , name='about') , 
    path('contact/' ,  Contact.as_view()) , 
    path('sendOtp/' ,  sendotp.sendOtp , name = 'sendotp') , 
]
