from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
app_name="adminApp"
urlpatterns = [
    path('',home,name='home'),
    path('new_cours/',newCours,name='new.cours'),
    path('new_cours/<slug:matiere>',newCours,name='new.cours.matiere'),
    path('edit_cours/<slug:slug>/',login_required(CourUpdateView.as_view()),name='update.cours'),
    path('new_matiere/',newMatiere,name='new.matiere'),
    path('delete_cours/<slug:slug>/<int:id>',login_required(CourDeleteView.as_view()),name='delete.cours'),
    path('delete_matiere/<slug:slug>/',login_required(MatiereDeleteView.as_view()),name='delete.matiere'),
    path('<slug:matiere>/',home,name='home.matiere'),
] 
