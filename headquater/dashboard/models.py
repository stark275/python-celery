from django.db import models

class Sale(models.Model):
    sale = models.CharField(max_length=200)
    sale_date = models.DateTimeField("date published")

