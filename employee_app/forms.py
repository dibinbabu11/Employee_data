from django import forms
from .models import Employee,Job,Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name',
                  'job',
                  'department',
                  'date_of_birth',
                  'basic_pay']
        