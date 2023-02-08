from django.db import models


class Product(models.Model):
    SIZE = (
        ('1', 'S'),
        ('2', 'M'),
        ('3', 'L'),
        ('4', 'XL'),
        ('5', 'XXL'),
    )
    name = models.CharField(max_length=20, verbose_name='')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='')
    discription = models.CharField(max_length=200, verbose_name='')
    color = models.CharField(max_length=20, verbose_name='')

class Order(models.Model):
    name = models.CharField(max_length=20,verbose_name='')
    phone_num = models.CharField(max_length=20,verbose_name='')
    adress = models.CharField(max_length=50, verbose_name='')
    




