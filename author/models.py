
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        verbose_name=_("Author Name"),
        max_length=100,
    )
    date_of_birth = models.DateField(
        verbose_name=_("Author Date Of Birth"),
    )
    country = CountryField()
