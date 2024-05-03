import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from myApp.models import Production
from myApp.serializer import ProductionSerializer


class ReadInfoView(APIView):
    def get(self, request, pk):
        try:
            production = Production.objects.get(id=pk)
            serializer = ProductionSerializer(production)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Production.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)