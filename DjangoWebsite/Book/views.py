from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def detail(request, name):
#     return HttpResponse("You're looking at question %s." % name)
def detail(request, name):
    return HttpResponse("You're looking at question %s" % name)
    # response = HttpResponse()
    # response.write("<h1>Xin chào các bạn</h1>")
    # response.write("BOOOOOOOKKKKK")
    # return response
