"""Model for actor"""
from django.db import models


class Actor(models.Model):
    """ Actor definitions. """
    name = models.CharField("Nombre del actor", max_length=255)

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        db_table = "actor"
        verbose_name = "Actor"
        verbose_name_plural = "Actores"

        indexes = [models.Index(fields=["name"], name="actor_name_idx")]

    def __str__(self):
        return f"{self.pk}. {self.name}"
