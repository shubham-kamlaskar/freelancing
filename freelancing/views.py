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

def form(request):
    finalans =0
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('username'))
            n2 = int(request.POST.get('password'))
            finalans = n1 + n2
            
    except Exception as e:
        finalans = e

    return render(request,"form.html",{'answer':finalans})