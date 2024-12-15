from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("viewProject", views.viewProject, name="viewProject"),
    path("getProject", views.getProject, name="getProject"),
    path("submitMSG", views.submitMSG, name="submitMSG")
]