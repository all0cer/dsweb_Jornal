# Generated by Django 5.0 on 2023-12-17 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jornal.noticia'),
        ),
    ]
