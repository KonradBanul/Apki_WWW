from rest_framework.response import Response
from rest_framework import status
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def person_list(request):
    if request.method == 'GET':
        persons = Osoba.objects.all()
        serializer = OsobaSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(request.method)
    if request.method == 'GET':
        person = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def job_list(request):
    if request.method == 'GET':
        jobs = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(jobs, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, sk):
    try:
        jobs = Stanowisko.objects.get(pk=sk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        jobs = Stanowisko.objects.get(pk=sk)
        serializer = StanowiskoSerializer(jobs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoSerializer(jobs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        jobs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
