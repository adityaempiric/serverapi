from django.shortcuts import render
from .models import TestModel
from .serializers import testModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response   

class TestView(APIView):
    def get(self,request):
        serializer = testModelSerializer(TestModel.objects.all(),many=True)
        return Response({
            'data' : serializer.data
        })

