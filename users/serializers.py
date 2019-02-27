from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('email', 'password', )


# class BusSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.CityInfo