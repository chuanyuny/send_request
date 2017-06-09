from django.shortcuts import render
import requests

# Create your views here.
def index(request):
	return render(request,'index.html')

def send_operation(request):
	targeturl=request.GET.get('url','')
	result=requests.get('http://'+targeturl)
	return render(request,'index.html',{'result':result})
