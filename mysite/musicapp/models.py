from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    age = models.IntegerField()

class Song(models.Model):
    Artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    title = models.CharField(max_length = 500)
    date_released = models.DateField(default = datetime.today)
    likes = models.IntegerField()
    artist_id = models.CharField(max_length = 500)


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.CharField(max_length = 2000)
    song_id = models.IntegerField()


