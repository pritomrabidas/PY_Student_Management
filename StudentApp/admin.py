from django.contrib import admin
from .models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "age","date_of_birth","religion",]
    search_fields = ["name", "email", "age","date_of_birth","religion",]
admin.site.register(Student,StudentAdmin)
admin.site.register(Subject)
admin.site.register(Hobby)
admin.site.register(Result)

