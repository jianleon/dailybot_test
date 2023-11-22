"""Model for movie"""

from django.db import models


class Movie(models.Model):
    """ Movie definitions. """
    title = models.CharField("Título", max_length=255)
    storyline = models.CharField("Línea de historia", max_length=255)
    content_rating = models.CharField("Rating de contenido", max_length=255)
    duration = models.CharField("Duración", max_length=255)
    release_date = models.DateField("Fecha de lanzamiento")
    poster_image = models.CharField("Imagen de poster", max_length=255)
    year = models.IntegerField("Año")

    actors = models.ManyToManyField("actor.Actor", verbose_name="Actores")
    genres = models.ManyToManyField("genre.Genre", verbose_name="Géneros")

    viewer_count = models.IntegerField("Contador de visitas")

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        db_table = "movie"
        verbose_name = "Película"
        verbose_name_plural = "Películas"

        indexes = [models.Index(fields=["title"], name="movie_title_idx")]

    def __str__(self):
        return f"{self.pk}. {self.title}"
