from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('locations', views.LocationViewset)
router.register('house_types', views.HouseTypeViewset)
router.register('houses', views.HouseViewset)
router.register('reviews', views.ReviewViewset)
router.register('rent_houses', views.RentHouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]