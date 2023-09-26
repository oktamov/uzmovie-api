from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=55)
    slug = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name.lower())
        return super().save(force_insert, force_update, using, update_fields)
