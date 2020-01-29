from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from polls.models import  Question


def index (request):
    html = "Hello world, That's polls' index"
    return HttpResponse(html)


def questions_list (request):
    qs = Question.objects.all()
    html=""
    for q in qs:
        html += str(q) + "<br>"
    return HttpResponse(html)


# Question.objects.get(id=2).

# widok podający question po podaniu id