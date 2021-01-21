from django.db import models

class EmpModel(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    date_naissance=models.CharField(max_length=100)
    salaire=models.IntegerField()
    genre=models.CharField(max_length=1)
    class Meta:
        db_table="employee"