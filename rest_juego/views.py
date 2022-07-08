from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from PrayTheNews.models import Juego,Usuario,Publicacion

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# api de publicaciones

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def lista_Publicaciones(request):
    if request.method == 'GET':
        Publicacions = Publicacion.objects.all()
        serializer = PublicacionSerializer(Publicacions,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarP(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = PublicacionSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlP(request,codigo):
    try:
        m = Publicacion.objects.get(idPublicacion = codigo)
    except Publicacion.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PublicacionSerializer(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = PublicacionSerializer(m,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# api de los Usuarios

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def lista_Usuarios(request):
    if request.method == 'GET':
        Usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(Usuarios,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarU(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlU(request,codigo):
    try:
        m = Usuario.objects.get(idUsuario = codigo)
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(m,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


# api Juegos
@csrf_exempt

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
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
@permission_classes((IsAuthenticated,))
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
@permission_classes((IsAuthenticated,))
def controlJ(request,codigo):
    try:
        m = Juego.objects.get(idJuego = codigo)
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


