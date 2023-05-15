from django.db import models

class Message(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField("date published")

class Sale(models.Model):
    sale = models.CharField(max_length=200)
    sale_date = models.DateTimeField("date published")

  