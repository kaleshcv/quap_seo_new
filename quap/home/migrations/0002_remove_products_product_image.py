# Generated by Django 3.2.7 on 2021-09-09 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_image',
        ),
    ]
