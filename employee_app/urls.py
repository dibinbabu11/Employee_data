from django.urls import path
from . import views

urlpatterns = [
    path("",views.employee_list,name='employee_list'),
    path("employee/create/", views.create, name="create"),
    path("employee/<int:emp_id>/update/", views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path("department/<int:dept_id>/", views.employees_by_department, name="employees_by_dept"),

]
