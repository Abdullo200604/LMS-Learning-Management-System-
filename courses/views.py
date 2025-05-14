# courses/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Kurslar ro'yxati yoki bosh sahifa.")
