from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RegistrarForm(models.Model):
    Id_login= models.AutoField(primary_key=True)
    nombre_us= models.CharField(max_length=100,db_column='nombre_us')
    apellidos_us = models.CharField(max_length=100,db_column='apellidos_us')
    correo_us =models.CharField(max_length=100,db_column='correo_us')
    contraseña=models.CharField(max_length=100,db_column='contraseña_us')
    rep_contra=models.CharField(max_length=100,db_column='rep_contra')
    class Meta:
        db_table='Registrar'

# class Precios(models.Model):
#      Id_precio= models.AutoField(primary_key=True)
#      precios= models.CharField(max_length=100,db_column='Precios')
#      class Meta:
#          db_table="Precios"
        
# class Empanadas(models.Model):
#      Id_empanadas= models.AutoField(primary_key=True)
#      empanadas= models.CharField(max_length=100,db_column='Empanadas')
#      class Meta:
#          db_table="Empanadas"
        
# class Cortes(models.Model):
#      Id_cortes= models.AutoField(primary_key=True)
#      cortes= models.CharField(max_length=100,db_column='Cortes')
#      class Meta:
#          db_table="Cortes"
        
# class Guarniciones(models.Model):
#      Id_guarniciones= models.AutoField(primary_key=True)
#      guarniciones= models.CharField(max_length=100,db_column='Guarniciones')
#      class Meta:
#          db_table="Guarniciones"
        

# class Postres(models.Model):
#      Id_postres= models.AutoField(primary_key=True)
#      postres= models.CharField(max_length=100,db_column='Postres')
#      class Meta:
#          db_table="Postres"
        

# class SalsaPastas(models.Model):
#      Id_salsapastas= models.AutoField(primary_key=True)
#      salsapastas= models.CharField(max_length=100,db_column='SalsaPasta')
#      class Meta:
#          db_table="SalsaPasta"
        
# class Cervezas(models.Model):
#      Id_cervezas = models.AutoField(primary_key=True)
#      cervezas= models.CharField(max_length=100,db_column='Cervezas')
#      class Meta:
#          db_table="Cervezas"
        
# class Refrescos(models.Model):
#      Id_refrescos = models.AutoField(primary_key=True)
#      refrescos= models.CharField(max_length=100,db_column='Refrescos')
#      class Meta:
#          db_table="Refrescos"
        
# class Cafes(models.Model):
#      Id_cafes= models.AutoField(primary_key=True)
#      cafes= models.CharField(max_length=100,db_column='Cafes')
#      class Meta:
#          db_table="Cafes"
        
class General(models.Model):
    Id_general = models.AutoField(primary_key=True)
    precios= models.CharField(max_length=100,db_column='Precios')
    empanadas= models.CharField(max_length=100,db_column='Empanadas')
    cortes= models.CharField(max_length=100,db_column='Cortes')
    guarniciones= models.CharField(max_length=100,db_column='Guarniciones')
    postres= models.CharField(max_length=100,db_column='Postres')
    salsapastas= models.CharField(max_length=100,db_column='SalsaPasta')
    alcohol= models.CharField(max_length=100,db_column='Alcohol')
    cervezas= models.CharField(max_length=100,db_column='Cervezas')
    refrescos= models.CharField(max_length=100,db_column='Refrescos')
    cafes= models.CharField(max_length=100,db_column='Cafes')
    class Meta:
        db_table="General"
    
