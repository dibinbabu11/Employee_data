from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    basic_pay = models.IntegerField( validators=[MinValueValidator(10000),MaxValueValidator(999999)])
    date_of_birth=models.DateField()
    
    @property
    def hra(self):
        return self.basic_pay * 0.10

    @property
    def da(self):
        return self.basic_pay * 0.25

    @property
    def gross_pay(self):
        return self.basic_pay + self.da + self.hra

    @property
    def pt(self):
        return self.basic_pay * 0.01

    @property
    def pf(self):
        return self.basic_pay * 0.12
    @property
    def net_pay(self):
        return self.gross_pay - self.pt - self.pf

    def __str__(self):
        return self.name 
    