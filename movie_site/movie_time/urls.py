from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSets, basename='movie')
router.register(r'users', UserProfileViewSets, basename='users')
router.register(r'country', CountryViewSets, basename='countries')
router.register(r'genre', GenreViewSets, basename='genres')


urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', MovieListAPIView.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('director/', DirectorAPIView.as_view(), name='director_list'),
    path('director/<int:pk>', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail')
]
