from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from common.models import Category


# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    movie_year = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=500)
    img_url = models.CharField(max_length=500)
    poster_url = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def num_likes(self):
        return self.liked.all().count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name.lower())
        return super().save(force_insert, force_update, using, update_fields)


RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


class Review(models.Model):
    full_name = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="child_comments")
    comment = models.TextField(blank=True, null=True)
