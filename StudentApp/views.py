from django.shortcuts import render,redirect
from .models import Student
from django.db.models import Q
import os
def firstFun(request):
    Students = Student.objects.all()
    if request.method == 'GET':
        data = request.GET.get('src')
        if data:
            Students = Student.objects.filter(Q(name__icontains=data) | Q(email__icontains=data))
    return render(request,'Home/Home.html',{'stu':Students})

def delete_prof(request,id):
    Students = Student.objects.get(id=id)
    if Students:
        if Students.image != 'def.jpeg':
            os.remove(Students.image.path)
        Students.delete()
    return redirect(firstFun)

def update(request):
    return render(request,'Home/studentfile.html')