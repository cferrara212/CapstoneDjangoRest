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
    fact_city_param = request.query_params.get('city')
    if fact_city_param == None:
        facts = HistoricFact.objects.all()
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
   


class factDetail(APIView):
    def get_object(self,pk):
        try:
            return HistoricFact.objects.get(pk=pk)
        except HistoricFact.DoesNotExist:
            raise Http404

    def get(self, pk):
        fact = self.get_object(pk)
        serializer= HistorcFactSerializer(fact)
        return Response(serializer.data)

    def put(self,request,pk):
        fact = self.get_object(pk)
        serializer = HistorcFactSerializer(fact, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,pk):
        fact = self.get_object(pk)
        fact.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


