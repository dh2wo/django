from django.db import models
from django.utils import timezone # 시간정보 모듈

# Create your models here.
class Movie(models.Model):
   genre = models.CharField(max_length = 20)
   movie_name = models.CharField(max_length = 100)
   movie_summary = models.TextField(null = False, blank = False)
   reg_date = models.DateTimeField(default = timezone.now)

class Review(models.Model):
  reviewer_name = models.CharField(max_length = 20)
  movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
  review_text = models.TextField(default = 'Anonymous')
  score = models.IntegerField(default = 0)
  reg_date = models.DateTimeField(default = timezone.now)