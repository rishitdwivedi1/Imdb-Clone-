from rest_framework import serializers
from .models import Movies,Actors,Producer


class MovieSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Movies
        fields = ['movie', 'year_of_release','producer','actor','plot']
        depth=1

class ActorSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Actors
        fields = ['name', 'gender','dob','bio']


class ProducerSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Producer
        fields = ['name', 'gender','dob','bio']

    