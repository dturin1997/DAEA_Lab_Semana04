from django.db import models

# Create your models here.
class Region(models.Model):
    region_nombre=models.CharField(max_length=100)
    pub_date=models.DateTimeField('date published')

class Candidato(models.Model):
    region=models.ForeignKey(Region, on_delete=models.CASCADE)
    candidato_nombre=models.CharField(max_length=100)
    candidato_edad=models.IntegerField()
    candidato_partido=models.CharField(max_length=100)