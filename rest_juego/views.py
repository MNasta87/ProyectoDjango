from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import JuegoSerializer,JuegoSerializer2
from PrayTheNews.models import Juego

# Create your views here.

@csrf_exempt

@api_view(['GET','POST'])
def lista_juegos(request):
    if request.method == 'GET':
        juegos = Juego.objects.all()
        serializer = JuegoSerializer(juegos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = JuegoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def agregarJ(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = JuegoSerializer2(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def controlJ(request,codigo):
    try:
        m = Juego.objects.get(codigoChip = codigo)
    except Juego.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = JuegoSerializer2(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = JuegoSerializer2(m,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
