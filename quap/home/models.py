from django.db import models

# Create your models here.

class StateCityList(models.Model):
    FIPSCode = models.IntegerField()
    state = models.CharField(max_length=100)
    stateAbbreviation = models.CharField(max_length=10)
    countyCode = models.CharField(max_length=10)
    countyName = models.CharField(max_length=100)
