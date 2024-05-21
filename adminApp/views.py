from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from SchoolApp.forms import CourForm, MatiereForm
from django.http import HttpResponseRedirect,HttpResponse
from adminApp.models import Cour, Matiere
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse,reverse_lazy
from django.views.generic import UpdateView,DeleteView

# Create your views here.
link="admin"
def root(request):
    context={
        'matieres':Matiere.objects.order_by("-id")
    }
    return redirect('user/',context=context)
    
@user_passes_test(lambda user:user.is_superuser)
def home(request,matiere=None):
    if not matiere:
        mat=Matiere.objects.order_by('-id').first()
    else:
        mat=get_object_or_404(Matiere,slug=matiere)
    context={
        'matieres':Matiere.objects.order_by('-id'),
        'cours':Cour.objects.filter(matiere=mat),
        'mat':mat
    }
    print(Cour.objects.filter(matiere=mat))
    return render(request,'adminApp/index.html',context=context)





@user_passes_test(lambda user:user.is_superuser)
def newCours(request,matiere=""):
    context={}
    error=None
    success=None
    if matiere:
        context['matiere']=get_object_or_404(Matiere,slug=matiere)
    if request.method=="POST":
        form=CourForm(request.POST,request.FILES)
        if request.FILES:
            type_f=(request.FILES)['file'].content_type
            if not (type_f in ['text/plain','application/pdf','video/mp4','video/mpeg','video/avi']):
                error="Type de fichier non pris en charge"
                return render(request,'adminApp/new.html',context={'form':form,'error':error,'success':success,'title':'Enregister un nouveau cours','link':link})
        if form.is_valid():
            form.cleaned_data
            c=form.save(commit=False)
            if Cour.objects.filter(slug=c.getSlug):
                error="ce cours existe deja dans la base"
            elif c.checked():
                c.save()
                success="Le cours a ete enregistrer avec success"
                form=CourForm(initial=context)
            else:
                error="La description et le fichier ne doivent pas etre vide en meme temps"  
        else:
            error="Le formulaire est invalide"
    else:
        form=CourForm(initial=context)
    return render(request,'adminApp/new.html',context={'form':form,'error':error,'success':success,'title':'Enregister un nouveau cours','link':link})

@user_passes_test(lambda user:user.is_superuser)
def newMatiere(request):
    error=None
    success=None
    if request.method=="POST":
        form=MatiereForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            mat=form.save(commit=False)
            test=Matiere.objects.filter(title=mat.title)
            slug=Matiere.objects.filter(slug=mat.getSlug)
            if any([test,slug]):
                error="Cette matiere existe deja"
            else:
                mat.save()
                success="La matiere a ete enregistrer avec success"
            form=MatiereForm()
        else:
            error="Le formulaire est invalid"
    else:
        form=MatiereForm()
    return render(request,'adminApp/new.html',context={'form':form,'error':error,'success':success,'title':'Enregistrer une Nouvelle matiere','link':link})

class CourUpdateView(UpdateView):
    model=Cour
    template_name="adminApp/new.html"
    form_class=CourForm
    success_url=reverse_lazy('adminApp:home')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context["title"]="Editer un cours"
        context["btn"]="Update"
        return context

class MatiereDeleteView(DeleteView):
    model=Matiere
    template_name="adminApp/delete.html"
    success_url=reverse_lazy('adminApp:home')

class CourDeleteView(DeleteView):
    model=Cour
    template_name="adminApp/delete.html"
    success_url=reverse_lazy('adminApp:home')