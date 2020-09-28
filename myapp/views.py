from django.shortcuts import render

# Create your views here.
def filter_demo(request):
    return render(request,"filter_demo.html",{"data":"Hello World",'a':10,'b':40,"num":10})