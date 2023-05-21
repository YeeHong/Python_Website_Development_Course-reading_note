from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def sayhello(request):
	return HttpResponse('Hello Django~')			# type url: 127.0.0.1:8000 => show: Hello Django~

def hello2(request, username):
	return HttpResponse('Hello ' + username)		# type url 127.0.0.1:8000/hello2/Tom => show: Hello Tom

def hello3(request, username):
	now = datetime.now()
	return render(request, "hello3.html", locals())	# render(request, 'name of template', (have to be dictionary???)) (reference: https://ithelp.ithome.com.tw/articles/10236351, https://pythonviz.com/basic/local-and-global-variables-in-python/)

def hello4(request, username):
	now = datetime.now()
	return render(request, "hello4.html", locals())
