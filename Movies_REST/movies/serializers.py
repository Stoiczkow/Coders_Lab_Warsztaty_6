from .models import Person, Movie, Role
from rest_framework import serializers

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'director')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields  = ('id', 'first_name', 'last_name')