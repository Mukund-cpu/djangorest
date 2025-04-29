from django.shortcuts import render
# Create your views here.
from .models import ApiTable
#optional
from rest_framework import status
from rest_framework.response import Response
from .serializers import Apiserializers
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        data = ApiTable.objects.all()
        serilaizer = Apiserializers(data, many=True)
        return Response(serilaizer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serilaizer = Apiserializers(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_200_OK)