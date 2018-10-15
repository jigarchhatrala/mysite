from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
@csrf_exempt
def home(req):
    if(req.POST):
        return 0;
    else:
        context={"message":"Welcome To Atmiyavidyadham"}
        return render(req,"home/index.html",context)
