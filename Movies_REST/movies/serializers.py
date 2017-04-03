from .models import Person, Movie, Role
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'director', 'actors')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields  = ('id', 'first_name', 'last_name')

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"