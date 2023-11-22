""" Contains MovieSerializer definition """
from rest_framework.serializers import ModelSerializer

from movie.models import Movie


class MovieSerializer(ModelSerializer):
    """ Defines MovieSerializer behaviour. """

    class Meta:  # pylint: disable=too-few-public-methods
        """ Defines serializer fields that are being used """

        model = Movie

        exclude = ()
