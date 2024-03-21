from django.shortcuts import render

def home(request):
    return render(request,"website/home.html")
def learn(request):
    return render(request,"website/learn.html")

def gallery(request):
    return render(request,"website/gallery.html")

def practice(request):
    return render(request,"website/practice.html")

def login(request):
    return render(request,"website/login.html")



