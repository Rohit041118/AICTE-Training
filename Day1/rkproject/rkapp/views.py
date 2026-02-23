from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Teacher

# Create your views here.
def about(request):
    name = "Rohit"
    result = f"<h1>Hello from {name}!</h1>"
    return HttpResponse(result)

def home(request):
    return render(request, 'home.html')

def index(request):
    Students = Student.objects.all()
    page_title = "Student info page..."
    context = {
        'Students': Students,
        'page_title': page_title
    }
    return render(request, 'index.html', context)


def teach(request):
    Teachers = Teacher.objects.all()
    page_title = "Teacher info page..."
    context = {
        'Teachers': Teachers,
        'page_title': page_title
    }
    return render(request, 'teach.html', context)
