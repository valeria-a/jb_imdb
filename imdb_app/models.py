from django.db import models


# Create your models here.
class Movie(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    director = models.ForeignKey('Director', models.RESTRICT, null=True, blank=True)
    actors = models.ManyToManyField('Actor', through='MovieActor')

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}"

    class Meta:
        db_table = 'movies'


class Actor(models.Model):

    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)

    movies = models.ManyToManyField('Movie', through='MovieActor')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'actors'


class MovieActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    salary = models.IntegerField()
    main_role = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f"{self.actor.name} in movie {self.movie.name}"


    class Meta:
        db_table = 'movie_actors'


class Director(models.Model):

    name = models.CharField(null=False, max_length=128)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'directors'

    def __str__(self):
        return f"{self.name} id:{self.id}"



