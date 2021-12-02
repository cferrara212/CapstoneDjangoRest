from django.shortcuts import render
from django.http.response import Http404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import HistoricFact
from .serializers import HistorcFactSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_facts(request):
    facts = HistoricFact.objects.all()
    fact_city_param = request.query_params.get('city', None)
    fact_id_param = request.query_params.get('id', None)
    if fact_city_param == None:
        if fact_id_param == None:
            facts = HistoricFact.objects.all()
    elif fact_id_param != None:
        facts = HistoricFact.objects.filter(id = fact_id_param)
    else:
        facts = HistoricFact.objects.filter(city = fact_city_param)

    serializer = HistorcFactSerializer(facts, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_facts(request):
    if request.method == 'POST':
        serializer = HistorcFactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        facts = HistoricFact.objects.filter(user_id = request.user.id)
        serializer = HistorcFactSerializer(facts, many=True)
        return Response(serializer.data)
   
@api_view(['GET'])
@permission_classes([AllowAny])   
def get_fact(request,pk):
    fact = HistoricFact.objects.get(pk= pk)
    serializer = HistorcFactSerializer(fact)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_fact(request,pk):
    fact = HistoricFact.objects.get(pk=pk)
    serializer = HistorcFactSerializer(fact, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_fact(request,pk):
    fact = HistoricFact.objects.get(pk=pk)
    fact.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)



