from django.db import models

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
    prime_id = models.AutoField(primary_key=True,unique=True, editable=False,null=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='image/',default='def.png')
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

    def _str_(self):
        return f'{self.name}"s Profile'