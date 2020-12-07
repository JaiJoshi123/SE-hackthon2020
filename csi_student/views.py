from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
#from .form import ProductForm

# Create your views here.
#from django.venv.Scripts.src.csi_student.models import Student


def all_students_details(request):
    queryset=Student.objects.all()
    context={
        "object_list":queryset
    }
    return render(request,"csi_student/all_students.html",context)

def chat_window_view(request):
    obj = get_object_or_404(Student, id=id)
    context = {
        "con": obj,
    }
    return render(request, "students/chat_window.html", context)

def about_me(request,id):
    obj= Student.objects.get(id=id)
    context={
        "con":obj,
    }
    return render(request, "csi_student/profile.html", context)