from django.db import models
from app_ufc.models import Sportman
from history_app.models import Turnir


class FutureFees(models.Model):
    sportman = models.ForeignKey(Sportman, on_delete=models.CASCADE)
    turnir = models.ManyToManyField(Turnir, verbose_name='')
    image = models.ImageField(verbose_name='', upload_to='photoFutureFees/%Y/%m/%d/')

    def __str__(self) -> str:
        return self.turnir


class PastFees(models.Model):
    turnir = models.ForeignKey(Turnir, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.turnir
    






            
