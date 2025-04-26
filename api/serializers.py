from rest_framework import serializers
from . models import ApiTable

class Apiserializers(serializers.ModelSerializer):
    class Meta:
        model = ApiTable
        fields = "__all__"