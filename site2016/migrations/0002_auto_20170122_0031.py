# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site2016', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'verbose_name': 'aluno', 'verbose_name_plural': 'alunos'},
        ),
        migrations.AddField(
            model_name='professor',
            name='titulo',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr.'), ('Dr.ª', 'Dr.ª')], max_length=10, verbose_name='título'),
        ),
    ]
