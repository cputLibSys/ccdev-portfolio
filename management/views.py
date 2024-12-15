from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
import os
# Create your views here.

def index(request):

    context ={  

    }
    template=loader.get_template("management/index.html")
    return HttpResponse(template.render(context, request))
