from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
def about(request):
    return request(request,'about.html')
def detaill(request):
    return render(request,'single_article.html')
