# Generated by Django 5.0.2 on 2024-03-11 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jugador',
            old_name='titulos',
            new_name='altura',
        ),
    ]
