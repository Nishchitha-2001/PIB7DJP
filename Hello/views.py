from django.shortcuts import render
from django.http import HttpResponse

from django import forms
from .forms import studentform
from .models import students

form = studentform()
my_dict={"insert_me":"Its lowest .... ","sr":"Start dust " , 'form':form}
# Create your views here.
def index(request):
    return HttpResponse("<h1> I started learning Django and its fun </h1>")
def Hello(request):
    if request.method == "POST" :
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = studentform()

    # return HttpResponse("<h2> I am coming from the applications urls.py file </h2>")
    return render(request,'Hello/Home.html',context=my_dict)

def list_view(request):
    context = {}
    context["dataset"] = students.objects.all()
    return render(request,"Hello/list_view.html",context)