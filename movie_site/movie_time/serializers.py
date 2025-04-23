from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name','director']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovielanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movielanguages
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieMomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieMoments
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','movie_name', 'movie_image', 'year', 'genre', 'country', 'status_movie',]

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_moments = MovieMomentsSerializer(read_only=True, many=True)
    movie_videos = MovielanguagesSerializer(read_only=True, many=True)
    stars = RatingSerializer(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()



    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_image', 'actor', 'types',
                  'movie_time', 'movie_trailer', 'movie_moments',
                  'description', 'movie_videos',
                  'status_movie','count_rating','avg_rating','stars']

    def get_avg_rating(self, obj ):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    directors_movie = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = Director
        fields = ['director_name','directors_movie']

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'