from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class StateCityList(models.Model):
    FIPSCode = models.IntegerField()
    state = models.CharField(max_length=100)
    stateAbbreviation = models.CharField(max_length=10)
    countyCode = models.CharField(max_length=10)
    countyName = models.CharField(max_length=100)

class StateCityListNew(models.Model):
    state = models.CharField(max_length=100)
    stateAbbreviation = models.CharField(max_length=10)
    county_or_city = models.CharField(max_length=100)
    img = models.ImageField(upload_to="cities/",default="cities/default.jpg")
    content = RichTextField(blank=True, null=True)
    faq_q_1 = models.CharField(max_length=500,null=True)
    faq_ans_1 = models.TextField(null=True)
    faq_q_2 = models.CharField(max_length=500, null=True)
    faq_ans_2 = models.TextField(null=True)
    faq_q_3 = models.CharField(max_length=500, null=True)
    faq_ans_3 = models.TextField(null=True)

    def __str__(self):
        return self.county_or_city


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

class Products(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    product_image = models.ImageField(upload_to="products/", default="products/default.jpg")
    def __str__(self):
        return self.product_name[:100]

class Brands(models.Model):
    brand_name = models.CharField(max_length=200,null=True)
class Years(models.Model):
    year_name = models.IntegerField()

class EmailSubscriptions(models.Model):
    email_id = models.EmailField(null=True)

class Customer(models.Model):
    year = models.IntegerField()
    part = models.CharField(max_length=200,null=True)
    brand = models.CharField(max_length=200,null=True)
    customer_name = models.CharField(max_length=200,null=True)
    customer_phone = models.CharField(max_length=200,null=True)
    customer_email = models.CharField(max_length=200,null=True)