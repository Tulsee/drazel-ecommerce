from django.db import models
from .beerChoices import BEER_COUNTRY_CHOICES, BEER_ABV_CHOICES, BEER_BRAND_CHOICES, BEER_CATEGORIES_CHOICES


def beer_images(instance, filename):
    return 'product/beer/{file_name}'.format(filename)


class Beer(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=200, choices=BEER_CATEGORIES_CHOICES)
    country_of_origin = models.CharField(
        max_length=100, choices=BEER_COUNTRY_CHOICES, blank=True, null=True)
    abv = models.CharField(
        max_length=100, choices=BEER_ABV_CHOICES, blank=True, null=True)
    brand = models.CharField(
        max_length=100, choices=BEER_BRAND_CHOICES, blank=True, null=True)
    volume = models.DecimalField(decimal_places=2, max_digits=6)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to=beer_images)

    def __str__(self):
        return self.name
