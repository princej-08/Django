from django.db import models

# Create your models here.

class ShopLogin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

