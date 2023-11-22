"""Helpers for movie"""
from actor.models import Actor
from genre.models import Genre
from movie.models import Movie
from rating.models import Rating


def create_movie_actors(movie: Movie, actors: list):
    """ Creates the movie actors and assign them to granted movie

    Parameters
    ----------

    movie: Movie model object
        Movie to assign actors

    actors: list(str)
        List of actors to add to movie

    """
    bulk_list = []
    temp_actors = {}

    for actor in actors:
        if actor not in temp_actors:
            temp_actors[actor] = Actor.objects.create(name=actor)

        bulk_list.append(temp_actors[actor])

    movie.actors.add(*bulk_list)


def create_movie_genres(movie: Movie, genres: list):
    """ Creates the movie genres and assign them to granted movie

    Parameters
    ----------

    movie: Movie model object
        Movie to assign actors

    genres: list(str)
        List of genres to add to movie

    """
    bulk_list = []
    temp_genders = {}

    for genre in genres:
        if genre not in temp_genders:
            temp_genders[genre] = Genre.objects.create(name=genre)

        bulk_list.append(temp_genders[genre])

    movie.genres.add(*bulk_list)


def create_movie_ratings(movie: Movie, ratings: list):
    """ Creates the movie ratings and assign them to granted movie

    Parameters
    ----------

    movie: Movie model object
        Movie to assign actors

    ratings: list(int)
        List of ratings to add to movie

    """
    Rating.objects.bulk_create(
        [Rating(movie=movie, rate=rate) for rate in ratings]
    )
