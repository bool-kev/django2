# Generated by Django 5.0.4 on 2024-05-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_alter_cour_options_alter_matiere_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cour',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Cours_file'),
        ),
    ]