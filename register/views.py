from django.shortcuts import render, redirect
from .models import Employee
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=request.POST['salary']
        position=request.POST['position']
        email=request.POST['email']
        phone=request.POST['phone']
        Employee.objects.create(first_name=first_name, last_name=last_name, salary=salary, position=position, email=email, phone=phone)
        messages.success(request, 'Employee added successfully')
        return redirect('index')
    else:
        data={
            'employee': Employee.objects.all()
        }
        return render(request, 'index.html', data)


def e_list(request):
    data={
        'employee': Employee.objects.all()
    }
    return render(request, 'e_list.html', data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')