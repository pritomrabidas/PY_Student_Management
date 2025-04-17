from django.shortcuts import render,redirect
from .models import Student,Hobby
from django.db.models import Q
from django.conf import settings
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

def updateprof(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
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
        is_Bangledeshi = request.POST.get('is_bangladeshi') == 'True'
        hobby = request.POST.get('hobby')

        # ✅ Only delete the image if a new one is uploaded
        if image:
            if student.image and student.image.name != 'def.jpeg':
                old_image_path = os.path.join(settings.MEDIA_ROOT, student.image.name)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
            student.image = image  # Replace with new image

        # ✅ Update hobby
        stu_hobby = Hobby.objects.create(name=hobby)

        # ✅ Update other fields
        student.name = name
        student.email = email
        student.father_name = father_name
        student.mother_name = mother_name
        student.age = age
        student.date_of_birth = date_of_birth
        student.religion = religion
        student.gender = gender
        student.roll = roll
        student.city = city
        student.is_Bangledeshi = is_Bangledeshi
        student.hobby = stu_hobby

        stu_hobby.save()
        student.save()
        return redirect(firstFun)

    return render(request, 'updateCart.html', {"stu": student})