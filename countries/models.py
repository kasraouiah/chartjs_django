from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    data = models.IntegerField()

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=255)
    money = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.name, self.money)
