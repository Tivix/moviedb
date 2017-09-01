from models import *
from api_connection import movie_details

def check_is_liked(request, movie_id):
    if request.user.is_authenticated:
        movie = Movie.objects.filter(movie_id=movie_id).first()
        return Like.objects.filter(movie=movie,user=request.user)
    else:
        return None

def add_movie_to_db(movie_id):
    raw_data = movie_details(movie_id)
    new_movie = Movie(
        movie_id=raw_data.id,
        title=raw_data.title,
        cover_url = raw_data.cover_url,
        rating=raw_data.rating,
    )
    new_movie.save()
    return new_movie
