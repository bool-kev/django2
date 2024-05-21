from adminApp.models import Cour,Matiere
from django import forms


class CourForm(forms.ModelForm):
    
    class Meta:
        model=Cour
        exclude=['id','view','slug']
        labels={
            "title":"Intitule du cours",
            "file":"fichier joint"
        }

class MatiereForm(forms.ModelForm):
    
    class Meta:
        model = Matiere
        fields=['title']

