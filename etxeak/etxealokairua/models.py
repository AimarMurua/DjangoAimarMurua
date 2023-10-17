from django.db import models

# Create your models here.

class Etxea(models.Model):
    e_izena = models.CharField(max_length=100)
    e_herria = models.CharField(max_length=100)
    e_pertsonakopurua = models.CharField(max_length=2)

    def __str__(self):
        return self.e_izena
    
class Pertsona(models.Model):
    p_nan = models.CharField(max_length=100)
    p_izena = models.CharField(max_length=100)
    p_emaila = models.CharField(max_length=100)

    def __str__(self):
        return self.p_izena
    
class Alokairua(models.Model):
    etxea_izena = models.ForeignKey(Etxea, on_delete = models.CASCADE)
    pertsona_izena = models.ForeignKey(Pertsona, on_delete = models.CASCADE)
    alokairu_data_hasiera = models.DateField(null = True)
    alokairu_data_amaiera = models.DateField(null = True)