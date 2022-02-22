from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks

def form(request):
    return render(request,"createtask.html")

def create(request):
    if(request.method=='POST'):
        name=request.POST['name']
        description=request.POST['description']
        t=Tasks(name=name,description=description)
        t.save()
    return redirect(alltasks)


def alltasks(request):
    tasks=Tasks.objects.all() 
    return render(request,"alltasks.html",{"tasks":tasks})

def delete(request):
    if(request.method=='POST'):
        t=Tasks.objects.get(id=request.POST['delete'])
        t.delete()
    return redirect(alltasks)

def edit(request):
    if(request.method=='POST'):
        t=Tasks.objects.get(id=request.POST['edit'])
        return render(request,"createtask.html",{'task':t})
    return redirect(alltasks)

def update(request):
    if(request.method=='POST'):
        t=Tasks.objects.get(id=request.POST['id'])
        t.name=request.POST['name']
        t.description=request.POST['description']
        t.save()
    return redirect(alltasks)
    
def search(request):
    if(request.method=='POST'):
        search=request.POST['search']
        t=Tasks.objects.filter(name__contains=search)
        return render(request,"alltasks.html",{'tasks':t})
    else:
        return redirect(alltasks)



    







