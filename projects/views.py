from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .form import ProjectForm
from .functions import handle_uploaded_file

# Create your views here.
def all_projects(request):
    queryset = Project.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "projects/all_projects.html", context)


def create_project_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
            '''
            context={
                'form':form
            }
            return render(request, "projects/create_project.html", context)'''
    else:
        form = ProjectForm()
        context={}
    '''
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        # a = form.cleaned_data["author"]
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, "projects/create_project.html", context)'''


def one_project_view(request,id):
    obj=Project.objects.get(id=id)
    context={
        "con":obj,
    }
    return render(request, "projects/one_project.html", context)
