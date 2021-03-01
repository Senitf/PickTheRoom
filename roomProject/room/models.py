from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50)

class Room(models.Model):
    keyword = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region')
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    distance = models.FloatField()
    charge = models.IntegerField()

    #image = models.ImageField()

    #1~5까지의 값
    distance_score = models.IntegerField()
    charge_score = models.IntegerField()
    rating_score = models.IntegerField()

    SAW_score = models.FloatField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-SAW_score', 'title']