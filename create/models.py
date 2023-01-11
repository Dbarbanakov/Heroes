from django.db import models

import datetime, time


class CharacterClass(models.Model):
    character_type = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.character_type}"


class Gear(models.Model):
    name = models.CharField(max_length=32, default="Gear")
    weapon = models.CharField(max_length=16, default="Sling")
    armor = models.CharField(max_length=16, default="Shirt")
    misc = models.CharField(max_length=16, default="Amulet")

    def __str__(self):
        return f"{self.name}"


class Avatar(models.Model):
    avatar = models.ImageField(upload_to="avatars", default="avatars/")
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Hero(models.Model):

    name = models.CharField(max_length=32)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now())

    def exp(self):
        return int(time.mktime(datetime.datetime.now().timetuple())) - int(
            time.mktime(self.created.timetuple())
        )

    def current_level(self):
        return Hero.exp(self) // 10000

    def __str__(self):
        return f"{self.name}"
