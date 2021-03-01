from django.db import models

class Room(models.Model):
    REGION_CHOICES = (
        ('서울', '서울'),
        ('경기', '경기도'),
        ('강원', '강원도'),
        ('충남', '충청남도'),
        ('충북', '충청북도'),
        ('전남', '전라남도'),
        ('전북', '전라북도'),
        ('제주', '제주도'),
    )
    region = models.CharField(max_length=5, choices=REGION_CHOICES, null=True)
    title = models.CharField(max_length=100, default="")
    rating = models.FloatField(default=0.0)
    distance = models.FloatField(default=0.0)
    charge = models.IntegerField(default=0)
    image = models.CharField(max_length=200, default="")

    #1~5까지의 값
    distance_score = models.IntegerField(default=0)
    charge_score = models.IntegerField(default=0)
    rating_score = models.IntegerField(default=0)

    SAW_score = models.FloatField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-SAW_score', 'title']