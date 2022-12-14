# Generated by Django 4.1.3 on 2022-11-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='offer_pic',
            field=models.URLField(blank=True, null=True, verbose_name='Снимка-оферта'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Град'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='employer',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Работодател'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='job_position',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='sponsor',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Спонсор'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Щат'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='wage',
            field=models.FloatField(blank=True, null=True, verbose_name='Заплащане'),
        ),
    ]
