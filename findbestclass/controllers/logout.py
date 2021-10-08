from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from findbestclass.models import Student , Institute;

def logout(request):
	request.session.clear()
	return redirect('/' , {'showLogout':False})