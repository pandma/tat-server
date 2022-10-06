from django.db import models
from ..Pages.models import Pages


class Subpages(models.Model):
    title = models.CharField(max_length=100)
    big_image = models.CharField(max_length=500)
    small_image = models.CharField(max_length=500)
    pages = models.ForeignKey(Pages, on_delete=models.CASCADE)
