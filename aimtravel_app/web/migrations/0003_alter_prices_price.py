# Generated by Django 4.1.3 on 2022-11-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='price',
            field=models.FloatField(),
        ),
    ]