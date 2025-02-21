from django.shortcuts import render,get_object_or_404, redirect
from . models import Employee,Job,Department
from .forms import EmployeeForm

# Create your views here.


def employee_list(request):
    employee=Employee.objects.all()
    return render(request,"employee.html",{"employee":employee})


def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EmployeeForm()
    return render(request, "create.html", {"form": form})


def update(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "create.html", {"form": form})
def delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')