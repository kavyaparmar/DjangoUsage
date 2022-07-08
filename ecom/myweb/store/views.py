from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import myform
import datetime

# Create your views here.
# def products(request):
#     products = Product.objects.all()
#     return render(request, 'products.html', {'products' : products})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

def home(request):
    context= {}

    form = myform(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    # else:
    #     return HttpResponse(request,"Enter Valid Inputs")

    context['form'] = form
    return render(request, 'home.html', context)

def template_example(request):
    context = {
        "data":"You are the best",
        "list":[1,2,3,4,5,6,7,8]
    }

    return render(request, 'example.html' ,context)

def view_example(request):
    now = datetime.datetime.now()
    html = "The Time is {}".format(now)
    return HttpResponse(html)