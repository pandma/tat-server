from django.db import models
from ..Subpages.models import Subpages


class Tasks(models.Model):

    TYPE_CHOICES = (
        ("0", "TASKLIST"),
        ("1", "CALENDAR"),
        ("2", "CARDGALERY"),
        ("3", "LIST"),
        ("4", "NOTES"),
    )
    STATUS_CHOICES = (
        ("0", "TODO"),
        ("1", "DONE"),
    )

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    text = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=100)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="TODO")
    subpages = models.ForeignKey(Subpages, on_delete=models.CASCADE)
