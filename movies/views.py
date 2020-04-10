from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    # try:
    #     movie = Movie.objects.get(id=movie_id)
    #     return render(request, 'movies/detail.html',{'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html',{'movie': movie})
    