from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def register(request):
    return HttpResponse("Up and running"),

def test(request):
    return HttpResponse("other endpoint")