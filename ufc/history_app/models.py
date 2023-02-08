from django.db import models


class Turnir(models.Model):
    title = models.CharField(max_length=200,verbose_name='')
    pub_date = models.DateTimeField(verbose_name='')

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
    
    def __str__(self):
        return self.title
    
class PeopleTurnir(models.Model):
    knowdown = models.CharField(max_length=10, verbose_name='')
    tot_strokes = models.CharField(max_length=10, verbose_name='')
    accent_hits = models.CharField(max_length=10, verbose_name='')
    tr_ground = models.CharField(max_length=10, verbose_name='')
    surr_attemps = models.CharField(max_length=10, verbose_name='')
    turnir = models.ForeignKey(Turnir, verbose_name='', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return self.knowdown
    
    
        


