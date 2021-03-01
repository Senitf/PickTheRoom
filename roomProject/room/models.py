from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    REGION_CHOICES = (
        ('서울', '서울'),
        ('경기', '경기'),
        ('강원', '강원'),
        ('충남', '충남'),
        ('충북', '충북'),
        ('전남', '전남'),
        ('전북', '전북'),
        ('제주', '제주'),
    )
    region = models.CharField(max_length=5, choices=REGION_CHOICES, blank=True)
    title = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(default=0.0)
    distance = models.CharField(max_length=100, blank=True)
    charge = models.IntegerField(default=0)
    image = models.CharField(max_length=200, blank=True)

    #1~5까지의 값
    distance_score = models.IntegerField(default=0)
    charge_score = models.IntegerField(default=0)
    rating_score = models.IntegerField(default=0)

    SAW_score = models.FloatField(default=0)

    scrap = models.ManyToManyField(User, related_name='scrap', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['region', '-SAW_score', 'title']