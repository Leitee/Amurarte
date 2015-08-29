# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlImg', models.ImageField(null=True, upload_to=b'photos')),
                ('calificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('fechaInicio', models.DateField()),
                ('fechaCierre', models.DateField()),
                ('alto', models.FloatField()),
                ('ancho', models.FloatField()),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='duenio',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
        migrations.AddField(
            model_name='disenio',
            name='postulante',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
        migrations.AddField(
            model_name='disenio',
            name='publicacion',
            field=models.ForeignKey(to='aplicacion.Publicacion'),
        ),
    ]
