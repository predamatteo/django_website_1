from django.db import models

# Create your models here.
class Prodotto(models.Model):
    nome = models.CharField(max_length=25)
    prezzo = models.FloatField()
    scorta = models.IntegerField()
    img_url = models.CharField(max_length=2083)
    fornitore = models.CharField(max_length=45)
    offerta = models.BooleanField(blank=False)
    prezzo_in_offerta = models.FloatField()
