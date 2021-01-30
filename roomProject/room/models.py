from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room-detail', args=[self.id])
    