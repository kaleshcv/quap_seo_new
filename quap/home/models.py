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
    content_sentence_1 = models.TextField(null=True)
    content_sentence_2 = models.TextField(null=True)
    content_sentence_3 = models.TextField(null=True)
    content_sentence_4 = models.TextField(null=True)
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
    price = models.FloatField(null=True)
    part_number = models.CharField(max_length=50,null=True)
    popular_product = models.BooleanField(default=False)

    spec_1_qn = models.CharField(max_length=50,null=True,blank=True)
    spec_1_ans = models.CharField(max_length=50, null=True,blank=True)
    spec_2_qn = models.CharField(max_length=50, null=True,blank=True)
    spec_2_ans = models.CharField(max_length=50, null=True,blank=True)
    spec_3_qn = models.CharField(max_length=50, null=True,blank=True)
    spec_3_ans = models.CharField(max_length=50, null=True,blank=True)
    spec_4_qn = models.CharField(max_length=50, null=True,blank=True)
    spec_4_ans = models.CharField(max_length=50, null=True,blank=True)
    spec_5_qn = models.CharField(max_length=50, null=True, blank=True)
    spec_5_ans = models.CharField(max_length=50, null=True, blank=True)
    spec_6_qn = models.CharField(max_length=50, null=True, blank=True)
    spec_6_ans = models.CharField(max_length=50, null=True, blank=True)
    spec_7_qn = models.CharField(max_length=50, null=True, blank=True)
    spec_7_ans = models.CharField(max_length=50, null=True, blank=True)
    spec_8_qn = models.CharField(max_length=50, null=True, blank=True)
    spec_8_ans = models.CharField(max_length=50, null=True, blank=True)
    spec_9_qn = models.CharField(max_length=50, null=True, blank=True)
    spec_9_ans = models.CharField(max_length=50, null=True, blank=True)
    spec_10_qn = models.CharField(max_length=50, null=True, blank=True)
    spec_10_ans = models.CharField(max_length=50, null=True, blank=True)

    warranty = models.CharField(max_length=200,default='Not Available')
    product_feature_1 = models.CharField(max_length=100,null=True,blank=True)
    product_feature_2 = models.CharField(max_length=100,null=True,blank=True)
    product_feature_3 = models.CharField(max_length=100,null=True,blank=True)
    product_feature_4 = models.CharField(max_length=100,null=True,blank=True)
    product_feature_5 = models.CharField(max_length=100, null=True, blank=True)
    product_feature_6 = models.CharField(max_length=100, null=True, blank=True)
    product_feature_7 = models.CharField(max_length=100, null=True, blank=True)
    product_feature_8 = models.CharField(max_length=100, null=True, blank=True)
    product_feature_9 = models.CharField(max_length=100, null=True, blank=True)
    product_feature_10 = models.CharField(max_length=100, null=True, blank=True)

    category_list =(
        ('Engine System','Engine System'),('Interior','Interior'),
        ('Body Parts','Body Parts'), ('Safety and Security','Safety and Security'),
        ('Suspension Systems','Suspension Systems'),('Wheels and Tires','Wheels and Tires')
    )
    category = models.CharField(max_length=100, choices=category_list,null=True)
    description = RichTextField(null=True)
    remarks = models.TextField(null=True,blank=True)

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

class State(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name
