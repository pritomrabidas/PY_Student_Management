from django.shortcuts import render

def firstFun(request):
    return render(request,'Home/Home.html')
