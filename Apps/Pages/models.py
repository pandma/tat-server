from django.db import models


class Pages(models.Model):

    title = models.CharField(max_length=100)
    big_image = models.CharField(max_length=500)
    small_image = models.CharField(max_length=500)
