from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):

    template=loader.get_template("blog/index.html")
    return HttpResponse(template.render({}, request))
