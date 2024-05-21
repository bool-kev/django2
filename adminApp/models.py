from typing import Collection, Iterable
from django.db import models
from django.forms import CharField
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
import mimetypes

# Create your models here.

class Matiere(models.Model):
    title=models.CharField(max_length=50,unique=True,verbose_name='Titre')
    slug=models.SlugField(unique=True,null=True)

    def __str__(self):
        return self.title
    
    @property
    def getSlug(self):
        return slugify(self.title.lower())
    
    def get_absolute_url(self):
        return reverse("user:matiere.vue", kwargs={"matiere": self.slug})
    
    def save(self, *args, **kwargs):
        self.title=self.title.title()
        self.slug=self.getSlug
        return super().save(*args,**kwargs)
    class Meta:
        verbose_name="Matiere"

class Cour(models.Model):
    title=models.CharField(max_length=50,verbose_name='Titre')
    description=models.TextField(blank=True)
    file=models.FileField(upload_to='Cours_files',null=True,blank=True)
    view=models.IntegerField(default=0)
    slug=models.SlugField(null=True)
    matiere=models.ForeignKey(Matiere,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def checked(self):
        return not (not self.file and not self.description)
    def getFile(self):
        # return f"Cours_file/{str(self.file).split('/')[-1]}"
        return self.file.url
    def get_absolute_url(self):
        return reverse("user:matiere.vue", kwargs={"matiere": self.slug})
    
    @property
    def getIcons(self):
        type=str(self.file).split('.')[-1]
        if  type=='pdf':
            return  "img/pdf.png"
        elif type=='txt':
            return  "img/text.png"
        elif type in ['mp3','mp4','mkv','wepm','flv','avi']:
            return  "img/video.png"
        else:
            return "img/default.png"

    def get_absolute_url(self):
        return reverse("user:cour.vue", kwargs={"matiere": self.matiere.slug,"cours":self.slug})
    
    def save(self, *args, **kwargs):
        self.title=self.title.title()
        self.slug=self.getSlug
        if self.checked():
            return super().save(*args,**kwargs)
    @property
    def getSlug(self):
        return slugify(f"{self.matiere.getSlug}-{self.title.lower()}")
    
    def clean_file(self):
        if self.file:
            file=self.cleaned_data['file']
            type=mimetypes.guess_type(file.name)
            if not type in ['text/plain','application/pdf','video/mp4','video/mpeg','video/avi']:
                raise ValidationError("Le type de fichier n'est pas supporter")
        return file
    class Meta:
        verbose_name="Cour"