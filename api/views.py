from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import ApiTable
from rest_framework import status
from rest_framework.response import Response
from .serializers import Apiserializers
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        data = ApiTable.objects.all()
        serilaizer = Apiserializers(data, many=True)
        return Response(serilaizer.data, status=status.HTTP_200_OK)