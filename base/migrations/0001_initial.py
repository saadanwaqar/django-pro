# Generated by Django 3.2.14 on 2022-11-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='divina_pagina_inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200000)),
                ('slug', models.SlugField()),
                ('doc', models.FileField(null=True, upload_to='divina-pagina-inicio')),
            ],
        ),
    ]
