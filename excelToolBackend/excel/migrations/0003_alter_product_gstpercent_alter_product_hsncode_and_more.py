# Generated by Django 4.2.7 on 2023-11-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0002_alter_product_gstpercent_alter_product_mrp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gstPercent',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='hsnCode',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='mrp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='productCategory',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='sellPrice',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]