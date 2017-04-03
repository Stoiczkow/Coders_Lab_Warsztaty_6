from django.shortcuts import render
from .models import Person, Movie, Role
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import MovieSerializer, PersonSerializer
# Create your views here.


class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieView(APIView):
    def get_object(self, id):
        try:
            return Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonsView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonView(APIView):
    def get_object(self, id):
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id):
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)