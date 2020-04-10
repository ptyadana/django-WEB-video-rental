from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Movie

def index(request):
    #all objects
    #SELECT * FROM movie_movie
    movies = Movie.objects.all()
    # output = ', '.join([movie.title for movie in movies])

    #filter
    #SELECT * FROM movie_movie WHERE released_year = 2000
    # Movie.objects.filter(released_year=2000)

    #specific object
    # Movie.objects.get(id=1)

    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html',{'movie': movie})