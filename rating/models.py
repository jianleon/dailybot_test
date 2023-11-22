"""Model for Rating"""
from django.db import models


class Rating(models.Model):
    """ Rating definitions. """
    movie = models.ForeignKey("movie.Movie", on_delete=models.CASCADE)
    rate = models.IntegerField("Calificación")

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        db_table = "rating"
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

        indexes = [models.Index(fields=["rate"], name="rating_rate")]

    def __str__(self):
        return f"{self.pk}. [{self.movie}] Rate: [{self.rate}]"
