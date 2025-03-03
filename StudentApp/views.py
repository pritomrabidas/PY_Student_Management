from django.shortcuts import render

def firstFun(request):
    return render(request,'index.html')
