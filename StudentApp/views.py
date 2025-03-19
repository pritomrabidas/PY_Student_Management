from django.shortcuts import render
from .models import Student
def firstFun(request):
    Students = Student.objects.all()
    return render(request,'Home/Home.html',{'stu':Students})
