# Generated by Django 4.2.7 on 2023-11-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gstPercent',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='mrp',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='sellPrice',
            field=models.CharField(max_length=100),
        ),
    ]
