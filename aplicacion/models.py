from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	fechaNacimiento = models.DateField()
	sexo = models.CharField(max_length=10)
	telefono = models.CharField(max_length = 20)
	user = models.OneToOneField(User)# one to one para que la relacion sea de uno a uno 

	def __str__(self):
		return self.user.username

#class Categoria(models.Model):
#	nombre = models.CharField(max_length= 50)
#	descripcion = models.CharField(max_length= 200)

#	def __str__(self):
#		return self.nombre


class Publicacion(models.Model):
	direccion = models.CharField(max_length=100)
	fechaInicio = models.DateField()
	fechaCierre = models.DateField()
	alto = models.FloatField()
	ancho = models.FloatField()
	descripcion = models.CharField(max_length = 300)
	duenio = models.ForeignKey(Usuario)
#	categoria = models.ForeignKey(Categoria)

	def __str__(self):
		return self.nombre
	

class Disenio(models.Model):
	postulante = models.ForeignKey(Usuario)
	publicacion = models.ForeignKey(Publicacion)
	urlImg = models.ImageField(upload_to = "photos", null = True)
	calificacion = models.IntegerField()

