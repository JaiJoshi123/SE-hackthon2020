from django.shortcuts import render,get_object_or_404,redirect
from .models import Question
from .models import Stud_Ans
from .form import Answer
from .form import New_Question_Form
from .form import Upvote
from django.db.models import F

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})

def about_view(request,*args,**kwags):
    return render(request,"about.html",{})

def forum_view(request):
    queryset = Question.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request,"forum.html",context)

def ans_view(request,id):
    try:
        queryset = Stud_Ans.objects.filter(q_id=id)
    except Stud_Ans.DoesNotExist:
        queryset=None
    obj= Question.objects.get(id=id)
    form=Answer(request.POST or None)
    if form.is_valid():
        #a=Stud_Ans(q_id=id).save()
        #print(a.id
            #  )
        Stud_Ans.objects.create(answer= form.cleaned_data["answer"], q_id=id)
        form.save()
        form=Answer()
    upvote_form = Upvote(request.POST or None)
    if upvote_form.is_valid():
        a=Stud_Ans.objects.get(id=id)
        a.total_upvotes = F('total_upvotes') + 1
        a.save()
        upvote_form.save()
    a = Stud_Ans.objects.get(id=id)
    context={
        "q_id":queryset,
        "con": obj,
        'ans_form':form,
        'upvote_form':upvote_form,
        'testing':a,
    }
    return render(request,"dynamic_questions.html",context)
def form_create_view(request,*args,**kwargs):
    form=New_Question_Form(request.POST or None)
    if form.is_valid():
        form.save()
    form=New_Question_Form()
    context={
        'question_form':form
    }
    return render(request,"question_create.html",context)
