from django.http import HttpRequest
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def find(request):
    return render(request,"find.html")

def login(request):
    return render(request,"login.html")

def payment(request):
    return render(request,"payment.html")

def products(request):
    return render(request,"products.html")