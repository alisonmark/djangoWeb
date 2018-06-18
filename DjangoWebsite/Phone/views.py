from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Category, iPhone, Sony

# Create your views here.

def index(request):
    # response = HttpResponse()
    # response.write("<h1>Xin chào các bạn</h1>")
    # response.write("<h2>List Of iPhone </h2>")
    # lstIPhone = iPhone.objects.all()
    # for i in lstIPhone:
    #     response.write(i.imodel + " - ")
    #     response.write(i.getCategory())
    #     response.write("<br>")
    # return response
    lstIPhone = iPhone.objects.all()
    template = loader.get_template("Phone/index.html")
    context = {
        'lstIPhone': lstIPhone,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'Phone/index.html', context)

def detail(request, phoneName):
    detailPhone = iPhone.objects.get(name__exact=phoneName)
    # phoneName = detailPhone.name
    # template = loader.get_template("Phone/detail.html")
    # context = {
    #     'detailPhone': detailPhone,
    # }
    # return HttpResponse(template.render(context, request))
    # return render(request, 'Phone/detail.html', context)
    # return render(request, 'Phone/404Page.html', None)
    try:
        # phoneName = detailPhone.name
        template = loader.get_template("Phone/detail.html")
        context = {
            'detailPhone': detailPhone,
        }
        # return HttpResponse(template.render(context, request))
        return render(request, 'Phone/detail.html', context)
    except iPhone.DoesNotExist:
        pass
        # raise Http404("Question does not exist")
        # raise Http404("No MyModel matches the given query.")
        # return render(request, 'Phone/404Page.html', None)
