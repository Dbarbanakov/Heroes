from django.db import models
from create.models import Hero


class Party(models.Model):
    member = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.member}"
