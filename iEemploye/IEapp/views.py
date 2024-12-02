from django.shortcuts import render
from django.http import HttpResponse
from . models import emp_info 
from django.core import validators
from IEapp import models

# Create your views here.

def create(request):
    if request.POST:
        name=request.POST.get('name')
        emid=request.POST.get('emid')
        role=request.POST.get('role')
        join=request.POST.get('join')
        emp_dls = emp_info(name=name,emid=emid,role=role,join=join)
        emp_dls.save()  
    return render(request,'create.html')

def list(request):
    emp_info_list = emp_info.objects.all()
    return render(request,'list.html',{"details": emp_info_list })
    
def edit(request,pk):
    instance_edit=emp_info.objects.get(pk=pk)
    frm=emp_info(instance=instance_edit)
    return render(request,'create.html')

def welcome(request):
    return render(request,'pag1.html')

def vryemail(request):
    form = models.forms_name()
    return render(request,'edit.html',{'form':form})

def delete(request,pk):
    instance=emp_info.objects.get(pk=pk)
    instance.delete()
    emp_info_list = emp_info.objects.all()
    return render(request,'list.html',{"details": emp_info_list })