from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    year = models.IntegerField()
    director = models.ForeignKey(Person)
    actors = models.ManyToManyField(Person, through=Role)


class Role(models.Model):
    role = models.CharField(max_length=256)
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
