from rest_framework import serializers
from . import models

class HouseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HouseType
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    house_type = HouseTypeSerializer()
    image = serializers.ImageField(max_length=None, use_url=True)
    posted_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.House
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class RentHouseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    house = serializers.StringRelatedField()

    class Meta:
        model = models.RentHouse
        fields = '__all__'