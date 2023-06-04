from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

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

def dice(request):
	dice_result = random.randint(1, 6)
	return render(request, "dice.html", {"dice_result_on_html":dice_result})

def dice2(request):
	no1 = random.randint(1, 6)
	no2 = random.randint(1, 6)
	no3 = random.randint(1, 6)
	return render(request, "dice2.html", locals())	# locals() means all variables in dice2 (including no1, no2, no3)

times=0  
def dice3(request):
	global times									# declare global variable
	times = times + 1
	local_times=times								# assign value to local variable: local_times
	username="David"
	dict_no={"no":random.randint(1,6)} #####??????看不懂，今天先到這邊吧…
	return render(request,"dice3.html",locals())

def show(request):
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    return render(request,"show.html",locals())

def filter(request):
	value=4
	list1=[1,2,3]
	pw="芝麻開門"
	
	html="<h1>Hello</h1>"
	value2=False
	return render(request,"filter.html",locals())