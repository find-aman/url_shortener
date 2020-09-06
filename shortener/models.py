from django.db import models
from .utils import code_generator, create_shortcode


class Shortener(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateField(auto_now=True)
    tmiestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Shortener, self).save(*args, **kwargs)
