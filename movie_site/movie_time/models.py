from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# from phonenumber_field.formfields import PhoneNumberField
from multiselectfield import MultiSelectField

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple')
)

class UserProfile(AbstractUser):
   age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                      MaxValueValidator(60)],
                                          null=True, blank=True)
   #phone_number = PhoneNumberField()
   status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='simple')

   def __str__(self):
       return f'{self.first_name}, {self.last_name}'

class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=96)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(75)])
    actor_image = models.ImageField(upload_to='actor_images/')

    def __str__(self):
        return self.actor_name

class Director(models.Model):
    director_name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(75)])
    director_image = models.ImageField(upload_to='director_images/')

    def __str__(self):
        return self.director_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=74)
    year = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor, related_name='actor_movie')
    director = models.ManyToManyField(Director, related_name='directors_movie')
    genre = models.ManyToManyField(Genre)
    TYPE_CHOICES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    types = MultiSelectField(max_length=43, choices=TYPE_CHOICES,  max_choices=5,)
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.URLField(null=True, blank=True)
    movie_image = models.ImageField(upload_to='movie_poster')
    status_movie = models.CharField(max_length=23, choices=STATUS_CHOICES)

    def __str__(self):
        return self.movie_name

    def get_avg_rating(self):
        rating = self.stars.all()
        if rating.exists():
            return round(sum([i.stars for i in rating]) / rating.count(), 1)
        return 0

    def get_count_rating(self):
        return self.stars.count()



class Movielanguages(models.Model):
    language = models.CharField(max_length=32, unique=True)
    video = models.FileField(upload_to='movie_videos/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_videos')

    def __str__(self):
        return f'{self.movie}, {self.language}'

class MovieMoments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_moments')
    movie_moments = models.ImageField(upload_to='movie_moments/')

    def __str__(self):
        return f'{self.movie}'

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='stars')
    stars = models.IntegerField(choices=[(i, str(i))for i in range(1, 11)])
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.movie}'

class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class FavoriteMovie(models.Model):
    fovorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)


