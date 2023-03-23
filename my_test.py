import os

os.environ["DJANGO_SETTINGS_MODULE"] = "imdb.settings"

import django
django.setup()

from imdb_app.models import *

# if __name__ == '__main__':
    # movie = Movie.objects.get(id=3)
    # actor = Actor.objects.get(id=1)


    # m = Actor.objects.filter(movies__director__name__icontains='tarantino')

    # movie = Movie.objects.get(id=3)
    # print(movie.actors.all())

