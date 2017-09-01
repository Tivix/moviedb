from . import api_connection
from . import helpers
import random

def search_page_context(request):
    try:
        query = request.GET['query'].replace(' ','%20')
    except Exception:
        query = None
    try:
        page = request.GET['page']
    except Exception:
        page = 1
    if query and query != '':
        context = api_connection.search_movie(query, page)
    else:
        context = api_connection.discover_movie(page)
    return context


def home_page_context(request):
    context = {
        'top20': api_connection.discover_movie(1)[0],
        'slideshow': api_connection.slideshow_movie()[0][:5],
    }
    return context

def movie_page_context(request, movie_id):
    similar = api_connection.similar_movie(movie_id)
    if len(similar)>3:
        similar = random.sample(similar)
    context = {
        'movie': api_connection.movie_details(movie_id),
        'is_liked': helpers.check_is_liked(request, movie_id),
        'similar': similar
    }
    return context

def account_page_context(request):
    i