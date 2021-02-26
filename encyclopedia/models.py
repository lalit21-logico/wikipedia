from django.db import models

# Create your models here.
class Entry(models.Model):
    ID = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=50)
    subheading = models.CharField(max_length=50)
    discription = models.CharField(max_length=250)