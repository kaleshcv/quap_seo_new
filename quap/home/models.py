from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class StateCityList(models.Model):
    FIPSCode = models.IntegerField()
    state = models.CharField(max_length=100)
    stateAbbreviation = models.CharField(max_length=10)
    countyCode = models.CharField(max_length=10)
    countyName = models.CharField(max_length=100)

class Blogs(models.Model):
    date_created = models.DateField()
    title = models.CharField(max_length=300)
    desc_1 = RichTextField(blank=True,null=True)
    desc_2 = RichTextField(blank=True,null=True)
    desc_3 = RichTextField(blank=True, null=True)
