# Generated by Django 5.2.1 on 2025-05-21 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_materiel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='accessoires',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_materiel.accessoire'),
        ),
    ]
