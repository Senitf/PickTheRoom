from django.db import models

class Condition(models.Model):
    distance = models.IntegerField()
    price = models.IntegerField()
    traffic = models.IntegerField()
    facility = models.IntegerField()
    usability = models.IntegerField()