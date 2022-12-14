from django.db import models
from model_utils import Choices


class JobOffer(models.Model):
    job_position = models.CharField(
        verbose_name='Позиция',
        max_length=30,
        blank=True,
        null=True,
    )
    employer = models.CharField(
        verbose_name='Работодател',
        max_length=30,
        blank=True,
        null=True,
    )
    wage = models.FloatField(
        verbose_name='Заплащане',
        blank=True,
        null=True,
    )
    city = models.CharField(
        verbose_name='Град',
        max_length=20,
        blank=True,
        null=True,
    )
    state = models.CharField(
        verbose_name='Щат',
        max_length=20,
        blank=True,
        null=True,
    )
    sponsor = models.CharField(
        verbose_name='Спонсор',
        max_length=15,
        blank=True,
        null=True,
    )
    offer_pic = models.URLField(
        verbose_name='Снимка-URL',
        blank=True,
        null=True,
    )
    job_description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        result = f'{self.job_position} at {self.employer} - {self.city}, {self.state}'
        return result


class Prices(models.Model):
    PRICING_TYPE = Choices('Self Arranged', 'Full Placement Standard', 'Premium Full Placement',)
    DEFAULT_PRICING_TYPE = 'Full Placement Standard'

    pricing_type = models.CharField(
        max_length=25,
        default=DEFAULT_PRICING_TYPE,
        choices=PRICING_TYPE,
        blank=True,
        null=True,
    )

    price = models.FloatField()

    price_description = models.TextField(
        blank=True,
        null=True,
        help_text="Please enter description"
    )

    def __str__(self):
        return f"{self.pricing_type}: $ {self.price:.2f}"


class AdditionalServices(models.Model):
    service_type = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    service_description = models.TextField(
        blank=True,
        null=True,
    )
    service_price = models.FloatField(
        blank=True,
        null=True,
    )