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
    main_image = models.ImageField(upload_to="images/",default="images/pexels-arnie-watkins-3156482.jpg")
    title = models.CharField(max_length=300)
    desc = models.TextField(default='QUAP')
    focus_content = models.TextField(default='QUAP')
    body = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=50, default='Team QUAP')
    tags = models.CharField(max_length=300, default='used auto parts')

    def __str__(self):
        return self.title[:100]