"""Model for Genre"""
from django.db import models


class Genre(models.Model):
    """ Genre definitions. """
    name = models.CharField("Nombre del género", max_length=255)

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        db_table = "genre"
        verbose_name = "Película"
        verbose_name_plural = "Películas"

        indexes = [models.Index(fields=["name"], name="genre_name_idx")]

    def __str__(self):
        return f"{self.pk}. {self.name}"
