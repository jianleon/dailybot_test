"""Unit test for queries"""
import json

from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from actor.models import Actor

from genre.models import Genre

from movie.models import Movie


DURATION_ENDPOINT = "/movie/duration"
YEAR_ENDPOINT = "/movie/year"


class MovieTestCase(TestCase):
    """ Tests for Movies GET endpoints. """

    def setUp(self):

        dracula_movie = Movie(
            title="Drácula",
            storyline="Película de vampiros",
            content_rating="G",
            duration="PM123M",
            release_date="1992-01-12",
            poster_image="an image url",
            year=1992,
            viewer_count=1000
        )
        dracula_movie.save()

        dracula_movie.actors.add(*[Actor(name="Keanu Rieves").save()])
        dracula_movie.genres.add(*[Genre(name="Suspense").save()])

        movie = Movie(
            title="Insideout",
            storyline="Película animada sobre emociones",
            content_rating="F",
            duration="PM121M",
            release_date="2020-01-12",
            poster_image="an image url",
            year=2020,
            viewer_count=50000
        )
        movie.save()

        movie.actors.add(*[Actor(name="Sofia").save()])
        movie.genres.add(*[Genre(name="Animated").save()])

    def test_year_top_to_down(self):
        """ Asserts if response retrieves the movies by year correctly. """
        client = APIClient()
        response = client.get(YEAR_ENDPOINT, {"sort": "top_to_down"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content)["data"][0]["title"], "Insideout")

    def test_duration_top_to_down(self):
        """ Asserts if response retrieves the movies by duration correctly. """
        client = APIClient()
        response = client.get(DURATION_ENDPOINT, {"sort": "top_to_down"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content)["data"][0]["title"], "Drácula")
