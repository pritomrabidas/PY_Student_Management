from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "age","date_of_birth","religion",]
    search_fields = ["name", "email", "age","date_of_birth","religion",]
admin.site.register(Student,StudentAdmin)

