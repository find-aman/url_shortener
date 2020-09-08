from django.db import models
from .utils import code_generator, create_shortcode
from django.conf import settings
from .validators import validate_url_endings

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class Shortener(models.Model):
    url = models.URLField(validators=[validate_url_endings])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Shortener, self).save(*args, **kwargs)

    def get_short_url(self, *args, **kwargs):
        url = getattr(settings, "WEEIT_URL")
        shortcode = self.shortcode
        return str(url + shortcode)
