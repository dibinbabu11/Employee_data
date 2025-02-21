from django.contrib import admin
from .models import Department,Employee,Job
# Register your models here.



admin .site.register(Department)

admin .site.register(Job)

admin .site.register(Employee)