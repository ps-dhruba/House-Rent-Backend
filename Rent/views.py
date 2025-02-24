from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LocationViewset(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HouseTypeViewset(viewsets.ModelViewSet):
    queryset = models.HouseType.objects.all()
    serializer_class = serializers.HouseTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class HousePagination(pagination.PageNumberPagination):
    page_size = 1 
    page_size_query_param = 'page_size'
    max_page_size = 100

class HouseViewset(viewsets.ModelViewSet):
    queryset = models.House.objects.all()
    serializer_class = serializers.HouseSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = HousePagination
    search_fields = ['title', 'description', 'location__location', 'house_type__type']
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RentHouseViewSet(viewsets.ModelViewSet):
    queryset = models.RentHouse.objects.all()
    serializer_class = serializers.RentHouseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]