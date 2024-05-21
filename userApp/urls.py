from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
app_name="user"
urlpatterns = [
    path('',homePage,name='root'),
    path('home/',home,name='home'),
    path('signup/',signUp,name='signup'),
    path('logout/',LogoutView.as_view(next_page="/"),name="logout"),
    path('<slug:matiere>/',matiere,name='matiere.vue'),
    path('<slug:matiere>/<slug:cours>/',cours,name='cour.vue'),
]
