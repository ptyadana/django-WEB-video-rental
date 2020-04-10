from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    #exclude the field from admin interface
    exclude = ('date_created', )
    list_display = ('id', 'title', 'number_in_stock', 'daily_rental_rate', 'genre')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

