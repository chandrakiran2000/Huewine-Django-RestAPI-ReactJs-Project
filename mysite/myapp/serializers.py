from rest_framework import serializers
# from .models import * # it imports all
from .models import Moviesdata

class MoviesdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviesdata
        # fields = '__all__'
        fields = ('id', 'moviename', 'heroname')