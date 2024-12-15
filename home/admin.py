from django.contrib import admin
from .models import Service, Project, Message 

# Register your models here.
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Message)

