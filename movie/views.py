"""Views to control movies APIs"""
import json
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from actor.models import Actor

from movie.helpers import paginate_content
from movie.helpers import create_movie_actors
from movie.helpers import create_movie_genres
from movie.helpers import create_movie_ratings

from movie.models import Movie

from movie.serializers import MovieSerializer


class PopulateApi(APIView):
    """ Defines the HTTP verbs to populate the database. """

    def post(self, request):
        """ Populates the database

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        Returns
        -------

        int: Response status code.

        """
        # pylint: disable=no-member, unused-argument
        workpath = os.path.dirname(os.path.abspath(__file__))
        movies = open(os.path.join(workpath, "movies.json"), encoding="utf-8")

        for movie_item in json.load(movies):
            actors = movie_item.pop("actors")
            genres = movie_item.pop("genres")
            ratings = movie_item.pop("ratings")

            movie_item["content_rating"] = movie_item.pop("contentRating")
            movie_item["release_date"] = movie_item.pop("releaseDate")
            movie_item["poster_image"] = movie_item.pop("posterImage")
            movie_item["viewer_count"] = movie_item.pop("viewerCount")

            movie = Movie.objects.create(**movie_item)

            create_movie_actors(movie, actors)
            create_movie_genres(movie, genres)
            create_movie_ratings(movie, ratings)

        return Response(status=status.HTTP_201_CREATED)


class DurationApi(APIView):
    """ Defines the HTTP verbs to retrieve the movies by duration. """

    @paginate_content()
    def get(self, request):
        """ Retrieves the movies by duration

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        Returns
        -------

        list(dict), int: Response status code.

        """
        # pylint: disable=no-member
        if "sort" not in request.GET:
            return Response({
                "msg": "Argument 'sort' must be sent"
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.GET["sort"] not in ["top_to_down", "down_to_top"]:
            return Response({
                "msg": "The allowed values for sor are 'top_to_down' and "
                       "'down_to_top"
            }, status=status.HTTP_400_BAD_REQUEST)

        movies = Movie.objects.all()

        if request.GET["sort"] == "top_to_down":
            movies.order_by("-duration")
        else:
            movies.order_by("duration")

        return Response({
            "count": movies.count(),
            "data": MovieSerializer(
                movies[self.pagination_start: self.pagination_end], many=True
            ).data
        }, status=status.HTTP_200_OK)


class SameActorApi(APIView):
    """ Defines the HTTP verbs to retrieve the movies by same actor. """

    @paginate_content()
    def get(self, request):
        """ Retrieves the ranked movies

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        Returns
        -------

        list(dict), int: Response status code.

        """
        # pylint: disable=no-member
        if "actor" not in request.GET:
            return Response({
                "msg": "Argument 'actor' must be sent"
            }, status=status.HTTP_400_BAD_REQUEST)

        actor = Actor.objects.filter(name=request.GET["actor"]).first()
        if not actor:
            return Response({
                "msg": "Actor not found"
            }, status=status.HTTP_404_NOT_FOUND)

        movies = Movie.objects.filter(actors=actor)

        return Response({
            "count": movies.count(),
            "data": MovieSerializer(
                movies[self.pagination_start: self.pagination_end], many=True
            ).data
        }, status=status.HTTP_200_OK)


class YearApi(APIView):
    """ Defines the HTTP verbs to retrieves the movies by its year. """

    @paginate_content()
    def get(self, request):
        """ Retrieves the movies by year

        Parameters
        ----------

        request: dict
            Contains http transaction information.

        Returns
        -------

        list(dict), int: Response status code.

        """
        # pylint: disable=no-member
        if "sort" not in request.GET:
            return Response({
                "msg": "Argument 'sort' must be sent"
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.GET["sort"] not in ["top_to_down", "down_to_top"]:
            return Response({
                "msg": "The allowed values for sor are 'top_to_down' and "
                       "'down_to_top"
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.GET["sort"] == "top_to_down":
            movies = Movie.objects.all().order_by("-year")
        else:
            movies = Movie.objects.all().order_by("year")

        return Response({
            "count": movies.count(),
            "data": MovieSerializer(
                movies[self.pagination_start: self.pagination_end], many=True
            ).data
        }, status=status.HTTP_200_OK)
