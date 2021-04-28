from django.db import models

# Create your models here.
class Grade(models.Model):
    libelle=models.CharField(max_length=30)
    class Meta:
        managed=False
        db_table='grades'
    def __str__(self):
        return self.libelle

class Personne(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE,null=False)
    class Meta:
        managed=False
        db_table='personnes'
    def __str__(self):
        return self.nom