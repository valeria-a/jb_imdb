import datetime
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "imdb.settings"

import django
django.setup()

from imdb_app.models import *

if __name__ == '__main__':
    # movies = Movie.objects.all()
    # movies = Movie.objects.filter(name='inception')
    # movies = Movie.objects.filter(id=1)
    # for movie in movies:
    #     # print(movie.name, movie.description)
    #     print(movie)

    # movie = Movie.objects.filter(id=1)[0]
    # movie.year = 2010
    # movie.save()

    # movie = Movie.objects.get(id=2)
    # movie.year = 1994
    # movie.description = "Some new description"
    # movie.save()

    # movie = Movie(name="Titanic", year=2000)
    # movie.save()

    # Movie.objects.create(description="dhgdjgsd", year=2000)

    # m = Movie.objects.get(description="dhgdjgsd").delete()

    # Movie(description="dsfsdsdf").save()

    # m = Movie.objects.get(name='Pulp fiction')
    # print(m.director)

    # d = Director.objects.all()[0]
    # print(d.movie_set.all())

    # new_d = Director.objects.create(name='Stieven Spielberg',
    #                                 birth_date=datetime.date(1956, 2, 3))
    # new_m = Movie(name='Jurasic park', director=new_d)
    # new_m.save()

    # new_m.director = new_d
    # new_m.save()

    # d = Director.objects.get(pk=4)
    # d.movie_set.create(name='E.T', year=1982)

    # d.movie_set.remove(Movie.objects.get(id=7))

    # Filters
    # movies = Movie.objects.filter(year__gte=2000) #>= lte >
    # movies = Movie.objects.filter(year__lt=2000)
    # movies = Movie.objects.filter(name__exact='the')
    # movies = Movie.objects.filter(name__iexact='pulp fiction')
    # movies = Movie.objects.filter(name__contains='pulp fiction') #  LIKE %dgdfg%
    # movies = Movie.objects.filter(name__icontains='u') # ILIKE %dgdfg%
    # movies = Movie.objects.filter(name__istartswith='P')
    # movies = Movie.objects.filter(id__in=[1, 3, 5])
    # movies = Movie.objects.filter(id__in=[1, 3, 5], year__gt=2000, name__icontains='a')
    # Movie  # Director
    # print(movies)
    # director = Director.objects.all()[0]
    # print(director.movie_set.all())
    # movies = Movie.objects.filter(director__name__icontains='tarantino')
    # print(movies)
    # movies = Movie.objects.filter(year=2030)
    # print(movies)
    # movie = Movie.objects.get(id=200)
    # print(type(movie))
    # print(movie)

    # try:
    #     movie = Movie.objects.get(id=500)
    #     print(type(movie))
    #     print(movie)
    # except Movie.DoesNotExist:
    #     print("does not exist")

    # movie = Movie.objects.filter(year=1994)
    # print(type(movie))
    # print(movie)

    # movies_query_set = Movie.objects.all()
    # print("The query is:", movies_query_set.query)
    # # for m in movies_query_set:
    # #     print(m)
    # # print(movies_query_set)
    # movies_query_set = movies_query_set.filter(year__gt=1999)
    # print("The query is:", movies_query_set.query)
    # movies_query_set = movies_query_set.exclude(name__icontains='h')
    # print("The query is:", movies_query_set.query)

    # movies_query_set = Movie.objects.all().filter(year__gt=1999).exclude(name__icontains='h')
    # print(movies_query_set.query)
    # movies_query_set = movies_query_set.exclude(director__name__icontains='a')
    # print(movies_query_set.query)
    pass


