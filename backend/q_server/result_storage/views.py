from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import *
# Create your views here.


class ResultsListView(APIView):
    def get(self, request):
        #results_data = Result.objects.all()
        results_data = Result.objects.order_by(F('sum') * F('percent'))[0:10]
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

def save_data(serialize_data):
    if serialize_data.is_valid():
        serialize_data.save()
        return Response("Данные сохранены", status=status.HTTP_200_OK)
    else:
        return Response(
            serialize_data.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
