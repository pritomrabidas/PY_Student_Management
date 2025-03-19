from django.db import models
class Hobby(models.Model):
    name = models.CharField(max_length=100)
    
    def _str_(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def _str_(self):
        return self.name

class Result(models.Model):
    mark = models.FloatField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    def _str_(self):
        return self.subject.name
    
class Student(models.Model):
    RELIGION = {
    "Hindu": "Hindu",
    "Muslim": "Muslim",
    "Christian": "Christian",
    "Buddhist": "Buddhist",
    "Others": "Others",
}
    GENDER = {
    "Male": "Male",
    "Female": "Female",
    "Others": "Others",
}
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='images/',default='def.png')
    mother_name= models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    religion = models.CharField(choices=RELIGION,max_length=20)
    gender = models.CharField(choices=GENDER,max_length=20)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    is_Bangledeshi = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ManyToManyField(Subject)
    result =models.ManyToManyField(Result)
    hobby =  models.OneToOneField(Hobby,on_delete=models.CASCADE, )

    def _str_(self):
        return f'{self.name}"s Profile'