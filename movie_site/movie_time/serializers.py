from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'status', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','first_name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name','director']


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id','actor_name' ]

class MovielanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movielanguages
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name',]

class MovieMomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieMoments
        fields = '__all__'

class DirectorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['id','director_name',]

class DirectorDetailSerializer(serializers.ModelSerializer):
    directors_movie = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = Director
        fields = ['id','director_name','directors_movie','age', 'bio']

class DirectorListMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['id','director_name']

class MovielistSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(read_only=True, slug_field='country_name')
    genre = GenreSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ['id','movie_name', 'movie_image', 'year', 'genre', 'country', 'status_movie',]

class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%y %H:%M '))
    user = UserProfileSerializer()
    movie = serializers.SlugRelatedField(read_only=True, slug_field='movie_name')

    class Meta:
        model = Rating
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_moments = MovieMomentsSerializer(read_only=True, many=True)
    movie_videos = MovielanguagesSerializer(read_only=True, many=True)
    stars = RatingSerializer(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()
    director = DirectorListMovieSerializer(read_only=True, many=True)
    actor = ActorListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['movie_name','director', 'movie_image', 'actor', 'types',
                  'movie_time', 'movie_trailer', 'movie_moments',
                  'description', 'movie_videos',
                  'status_movie','count_rating','avg_rating','stars',]

    def get_avg_rating(self, obj ):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()



class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movie = MovielistSerializer(read_only=True, many=True)

    class Meta:
        model = Actor
        fields = '__all__'

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'