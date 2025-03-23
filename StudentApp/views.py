from django.shortcuts import render,redirect
from .models import Student,Hobby
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

def create_prof(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST.get('email')
        image = request.FILES.get('image')
        father_name = request.POST.get('father_name')    
        mother_name = request.POST.get('mother_name')
        age = request.POST.get('age')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        gender = request.POST.get('gender') 
        roll = request.POST.get('roll')
        city = request.POST.get('city')
        is_Bangledeshi = request.POST.get('is_Bangledeshi' ,'True')
        # subject = request.POST.get('subject')
        # result = request.POST.get('result')
        hobby = request.POST.get('hobby')
        stu_hobby = Hobby.objects.create(name=hobby)
        student = Student(name=name,email=email,image=image,father_name=father_name,mother_name=mother_name,age=age,date_of_birth=date_of_birth,religion=religion,gender=gender,roll=roll,city=city,is_Bangledeshi=is_Bangledeshi,hobby=stu_hobby)

        stu_hobby.save()
        student.save()
        return redirect(firstFun)
    return render(request,'Home/studentfile.html')