from asyncio.windows_events import NULL
from contextlib import nullcontext
from email.policy import default
from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=10)
    salary = models.IntegerField()
    address = models.CharField(max_length=100,null=True)

class Base:
    empno = models.IntegerField(null = True)
    address = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Canteen(Base):
    tifin_menu = models.CharField(max_length=20)


class Product(models.Model):
    prdId = models.IntegerField(primary_key=True)
    prdname  = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/')
    price = models.IntegerField(null = True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.prdname
