# Generated by Django 3.2.11 on 2022-01-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]