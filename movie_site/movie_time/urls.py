from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', DirectorViewSets, basename='directors')
router.register(r'movie', MovieViewSets, basename='movies')
router.register(r'users', UserProfileViewSets, basename='users')
router.register(r'country', CountryViewSets, basename='countries')
router.register(r'actor', ActorViewSets, basename='actors')
router.register(r'genre', GenreViewSets, basename='genres')


urlpatterns = [
    path('api/', include(router.urls))
]
