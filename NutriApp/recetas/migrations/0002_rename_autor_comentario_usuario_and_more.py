# Generated by Django 4.2.6 on 2023-10-10 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='autor',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='autor',
            new_name='usuario',
        ),
    ]
