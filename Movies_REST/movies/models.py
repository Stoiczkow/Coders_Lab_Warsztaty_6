from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    year = models.IntegerField()
    director = models.ForeignKey(Person, related_name='director')
    actors = models.ManyToManyField(Person, through='Role', related_name='actor')


class Role(models.Model):
    role = models.CharField(max_length=256)
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)

