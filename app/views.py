from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jamPandu(request):
    return HttpResponse('<h1><marquee>From JamPandu To JigelRani: Hi How are You I Want Kernal Threads</h1></marquee>')

def jigelrani(request):
    return HttpResponse('<h1><marquee>Reply:I am Not Kernal I am User Defined Thread</h1></marquee>')



