from django.shortcuts import render
from projet.models import EmpModel
from django.contrib import messages
from projet.forms import Empforms


def index(request):
    tous=EmpModel.objects.all()
    return render(request,'index.html',{"donnee":tous})

def insert(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('prenom') and request.POST.get('date_naissance') and request.POST.get('salaire') and request.POST.get('genre'):
            savemploy=EmpModel()
            savemploy.nom=request.POST.get('nom')
            savemploy.prenom=request.POST.get('prenom')
            savemploy.date_naissance=request.POST.get('date_naissance')
            savemploy.salaire=request.POST.get('salaire')
            savemploy.genre=request.POST.get('genre')
            savemploy.save()
            messages.success(request,'Employee '+savemploy.prenom+' est enregistrer avec success')
            return render(request,'insert.html')
    else:
            return render(request,'insert.html')   

def edit(request,id):
    editemploy=EmpModel.objects.get(id=id)
    return render(request,'edit.html',{"edit":editemploy})     

def update(request,id):
    updateemploy=EmpModel.objects.get(id=id)
    form=Empforms(request.POST,instance=updateemploy)
    if form.is_valid():
        form.save()
        messages.success(request,'Employee Update Successfully')
        return render(request,'edit.html',{"edit":updateemploy})