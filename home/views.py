from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
from .collectfiles import *
import os
import shutil

class SKILL():
   def __init__(self, name, color, xp):
      self.name=name
      self.color=color
      self.xp=xp

# Create your views here.
def index(request):
   
    skills=[SKILL('C++', '#42047E', 3), SKILL('Javsacript', '#382592', 4),SKILL('HTML 5', '#2E46A6', 5), SKILL('CSS', '#2567BA', 4), SKILL('Python', '#1B87CD', 5), SKILL('AngularJs', '#07C9F5', 2), SKILL('C', '#11A8E1', 3)]
    services = Service.objects.all().values() 
    projects = Project.objects.all().values()
    print('\n',services,'\n')
    context ={  
        'skills':skills,
        'services': services, 
        'projects': projects
    }
    template=loader.get_template("home/index.html")
    return HttpResponse(template.render(context, request))

def viewProject(request):
    if request.method=="GET":
        
        resp=list(Project.objects.all().filter(name=request.GET["name"]).values())
        fs=FileSystem()

        resp.append(fs.getFiles(os.path.join(fs.rootdir, resp[0]["files"])))
        
        return JsonResponse(resp, safe=False)


def getProject(request):
    if request.method=="GET":

        save_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'projects', request.GET["project_name"])
        download_dir=os.path.join('static', 'projects', request.GET["project_name"])+".zip"
        if not os.path.exists(save_dir+".zip"):

            archive = shutil.make_archive(save_dir,"zip", save_dir)

            return JsonResponse({"download_dir": download_dir})
        
        else:

            return JsonResponse({"download_dir": download_dir})


def submitMSG(request):
    if request.method=="GET":
        name=request.GET['name']
        email=request.GET['email']
        msg=request.GET['message']
        print('D 1')
        new_msg=Message(name=name, email=email, message=msg)
        new_msg.save()
        print('D 2')
        return JsonResponse({"success": True})