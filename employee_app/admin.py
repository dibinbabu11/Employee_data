from django.contrib import admin
from .models import Department, Job, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'emp_id',
        'name',
        'job',
        'department',
        'basic_pay',
        'gross_pay',
        'net_pay',
    )

    list_filter = ('department', 'job')
    search_fields = ('name', 'emp_id')
    ordering = ('name',)

    readonly_fields = (
        'hra',
        'da',
        'gross_pay',
        'pt',
        'pf',
        'net_pay',
    )

    fieldsets = (
        ("Employee Info", {
            "fields": ('emp_id', 'name', 'date_of_birth')
        }),
        ("Job Details", {
            "fields": ('job', 'department')
        }),
        ("Salary Details", {
            "fields": (
                'basic_pay',
                'hra',
                'da',
                'gross_pay',
                'pt',
                'pf',
                'net_pay',
            )
        }),
    )
