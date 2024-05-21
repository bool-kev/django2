from django.contrib import admin
from adminApp.models import Cour,Matiere
# Register your models here.
@admin.register(Cour)
class CourAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        "title",
        "description",
        "file",
        "view",
        "slug",
        "matiere",
    ]
    list_editable=['title','description','file','matiere']
    list_display_links=['id']
@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display=['id','title','slug']
    list_editable=['title']
    list_display_links=['id']