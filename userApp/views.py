
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import logout
from adminApp.models import Matiere,Cour
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def homePage(request):
    return render(request,'userApp/home.html')

@login_required
def home(request):
    cours=Cour.objects.order_by('-view')[:8]
    return render(request,'userApp/index.html',context={'Vue':"Most View courses",'matieres':Matiere.objects.all(),'cours':cours})


@login_required
def matiere(request,matiere):
    mat=get_object_or_404(Matiere,slug=matiere)
    return render(request,'userApp/index.html',context={'Vue':mat.title,'cours':mat.cour_set.all,'matieres':Matiere.objects.all()})

@login_required
def cours(request,matiere,cours):
    mat=get_object_or_404(Matiere,slug=matiere)
    cour=get_object_or_404(Cour,matiere=mat,slug=cours)
    cour.view+=1
    cour.save()
    if cour.file:
        type=str(cour.file).split('.')[-1]
        if type in ['mp3','mp4','mkv','wepm','flv','avi']:
            return render(request,'userApp/videoCourses.html',context={'cour':cour})
        elif type=="pdf":
            return render(request,'userApp/pdfCourses.html',context={'cour':cour})
    return render(request,'userApp/show.html',context={'cour':cour})

def signUp(request):
    error=None
    success=None
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            success="Inscription Reussie avec success"
            form.save()
            form=UserCreationForm()
        else:
            error="Une erreur s'est produite"
    else:
        form=UserCreationForm()
    return render(request,'adminApp/new.html',context={'form':form,'error':error,'success':success,'title':'Singn Up','link':'user'})

def logout(request):
    logout(request)
    return redirect('')