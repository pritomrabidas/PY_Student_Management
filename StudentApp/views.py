from django.shortcuts import render
from .models import Student
from django.db.models import Q
def firstFun(request):
    Students = Student.objects.all()
    if request.method == 'GET':
        data = request.GET.get('src')
        if data:
            Students = Student.objects.filter(Q(name__icontains=data) | Q(email__icontains=data))
    return render(request,'Home/Home.html',{'stu':Students})
