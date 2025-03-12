from django.shortcuts import render
from .models import Employee

def index(request):
    return render(request, 'index.html')

from .models import Employee

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        email = request.POST['email']
        phone = request.POST['phone']

        emp = Employee(
            name=name,
            city=city,
            state=state,
            country=country,
            email=email,
            phone=phone
        )
        emp.save()

        return render(request, 'thankyou.html', {'employee': emp})
    return render(request, 'register.html')
    

def members(request):
    all_employees = Employee.objects.all()
    return render(request, 'members.html', {'employees': all_employees})
