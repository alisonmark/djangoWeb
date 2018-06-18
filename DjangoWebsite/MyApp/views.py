from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	response = HttpResponse()
	response.write("<h1>Xin chào các bạn</h1>")
	response.write("Đây là ứng dụng đầu tiên của bố mày")
	return response
