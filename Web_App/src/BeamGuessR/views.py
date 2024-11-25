from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, wolrd. You're in Ohio... Always has been...")
