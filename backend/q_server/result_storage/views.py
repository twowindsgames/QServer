import math

from django.http import Http404
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import *
from django.db.models.functions import Sqrt
# Create your views here.



class ResultsListView(APIView):
    def get(self, request):
        #results_data = Result.objects.all()[0:100]
        #results_data = Result.objects.order_by(F('percent') * Sqrt(F('sum')) / F('day_count')).reverse()
        results_data = Result.objects.order_by(F('percent') + F('day_count')*0.013 + Sqrt(F('sum')) /30/ F('day_count')).reverse()
        results_data = results_data[ 0:100 ]
        serializer = ResultsSerializer(results_data,  many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request)
        query = JSONParser().parse(request)
        serialize_data = ResultsSerializer(data=query)
        return save_data(serialize_data)

    def delete( self, request ):
        results_data = Result.objects.all()
        results_data.delete()
        return Response("all delete")

class ResultsDetailView(APIView):
    def delete( self, request ):
        result_id= request.query_params.get('result_id', None)
        try:
            results_data = Result.objects.get(id=result_id)
            results_data.delete()
            return Response("delete")
        except Result.DoesNotExist:
            raise Http404

class MixResultsListView(APIView):
    def get(self, request):
        #results_data = MixResult.objects.order_by(F('percent') + F('in_candle') / 300/F('day_count') ).reverse()
        results_data = MixResult.objects.order_by(F('percent') + F('day_count')*0.013 + Sqrt(F('sum')) /30/ F('day_count')).reverse()
        results_data = results_data[ 0:100 ]
        serializer = MixResultsSerializer(results_data,  many=True)
        return Response(serializer.data)

    def post( self, request ):
        print(request)
        query = JSONParser().parse(request)
        serialize_data = MixResultsSerializer(data=query)
        return save_data(serialize_data)

    def delete( self, request ):
        results_data = MixResult.objects.all()
        results_data.delete()
        return Response("all delete")

def save_data(serialize_data):
    if serialize_data.is_valid():
        serialize_data.save()
        return Response("Данные сохранены", status=status.HTTP_200_OK)
    else:
        return Response(
            serialize_data.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
