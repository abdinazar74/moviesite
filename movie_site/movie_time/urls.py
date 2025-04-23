from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSets, basename='movie')
router.register(r'users', UserProfileViewSets, basename='users')
router.register(r'country', CountryViewSets, basename='countries')
router.register(r'actor', ActorViewSets, basename='actors')
router.register(r'genre', GenreViewSets, basename='genres')


urlpatterns = [
    path('api/', include(router.urls)),
    path('', MovieListAPIView.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('<int:pk>/director', DirectorAPIView.as_view(), name='directors_movie')
]
