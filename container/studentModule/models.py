from django.db import models

class Student(models.Model):
    name = models.TextField()
    crated_at = models.DateTimeField("date created")

