from django.shortcuts import render
from .models import Person, Movie, Role
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
# Create your views here.


class MoviesView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

