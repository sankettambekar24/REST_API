from rest_framework import serializers
from .models import blog, comment



class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'


class blogSerializer(serializers.ModelSerializer):
    comments =commentSerializer(many= True,read_only=True)
    class Meta:
        model= blog
        fields= '__all__'

