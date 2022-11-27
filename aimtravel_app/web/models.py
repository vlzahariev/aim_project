from django.db import models
from model_utils import Choices


class JobOffer(models.Model):
    state = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    city = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    job_position = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    employer = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    sponsor = models.CharField(
        max_length=15,
        blank=False,
        null=False,
    )

    wage = models.FloatField(
        blank=False,
        null=False,
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

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Please enter description"
    )

    def __str__(self):
        return f"{self.pricing_type}: $ {self.price:.2f}"
