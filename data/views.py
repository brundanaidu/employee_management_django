from django.shortcuts import render, redirect
from .models import employee
from django.db.models import F

# Create your views here.

def index(request):
    Employee = employee.objects.all()

    context = {'Employee': Employee}

    return render(request, 'index.html', context)
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        dob = request.POST['dob']
        company = request.POST['company']
        department = request.POST['department']
        skills = request.POST.getlist('skills')
        salary = request.POST['salary']
        address = request.POST['address']

        data = employee(name=name, email=email, age=age, gender=gender, dob=dob, company=company, department=department, skills=skills, salary=salary, address=address)
        data.save()
        return redirect('index')
    return render(request, 'create.html')

def delete(request, pk):
    emp = employee.objects.get(id=pk)
    emp.delete()
    return redirect('index')

def edit(request, pk):
    edit_employee = employee.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        dob = request.POST['dob']
        company = request.POST['company']
        department = request.POST['department']
        skills = request.POST.getlist('skills')
        salary = request.POST['salary']
        address = request.POST['address']

        edit_data = employee(id=pk, name=name, email=email, age=age, gender=gender, dob=dob, company=company, department=department, skills=skills, salary=salary, address=address)
        edit_data.save()
        return redirect('index')
    context = {'edit_employee': edit_employee}
    return render(request, 'edit.html', context)

def view(request, pk):
    view_employee = employee.objects.get(id=pk)

    context = {'view_employee': view_employee}
    return render(request, 'view.html', context)
