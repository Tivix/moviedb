import urllib2
import json

HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

API_KEY = 'f1e8949fba9ef7fd860c87edfc772fa9'


class JsonData:

    def __init__(self, json_data):
        self.page = json_data['page']
        self.total_pages = json_data['total_pages']
        self.results = json_data['results']

class JsonMovie:

    def __init__(self,json_data):
        self.results = json_data


class BasicMovie(object):

    def __init__(self, json_data):
        self.id = json_data['id']
        self.rating = json_data['vote_average']
        self.title = json_data['title']
        self.overview = json_data['overview']
        try:
            self.cover_url = 'http://image.tmdb.org/t/p/w342/' + json_data['poster_path']
        except Exception:
            self.static_cover = True
            self.cover_url = 'static/static_test.jpg'


class DetailsMovie(BasicMovie):

    def __init__(self, json_data):
        super(DetailsMovie, self).__init__(json_data)
        self.genres = [ genre['name'] for genre in json_data['genres']]


def json_responder(url, parameters={}):
    '''
    :param url: Url address to API
    :param parameters: Dict with query parameters
    :return: API response
    '''
    url += 'api_key='+API_KEY
    for key, value in parameters.items():
        url += '&'+str(key) + '=' + str(value)
    req = urllib2.Request(url, headers=HEADER)
    json_obj = urllib2.urlopen(req)
    data = json.load(json_obj)
    try:
        data = JsonData(data)
    except Exception:
        data = JsonMovie(data)
    except Exception:
        data = None
    return data


def discover_movie(page):
    url = 'https://api.themoviedb.org/3/discover/movie?'
    raw_data = json_responder(url, {
        'page': page,
    })
    if raw_data:
        movies = [BasicMovie(result) for result in raw_data.results]
        return [movies, raw_data.total_pages, raw_data.page]
    else:
        return None

def similar_movie(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{movie_id}/similar?'.format(movie_id=movie_id)
    raw_data = json_responder(url)
    if raw_data:
        movies = [BasicMovie(result) for result in raw_data.results]
        return movies
    else:
        return None


def search_movie(query, page):
    url = 'https://api.themoviedb.org/3/search/movie?'
    raw_data = json_responder(url, {
        'page': page,
        'query': query
    })
    if raw_data:
        movies = [BasicMovie(result) for result in raw_data.results]
        return [movies, raw_data.total_pages, raw_data.page]
    else:
        return None


def slideshow_movie():
    url = 'https://api.themoviedb.org/3/movie/popular?'
    raw_data = json_responder(url, {
        'sort_by': 'primary_release_date.desc',
    })
    if raw_data:
        movies = [BasicMovie(result) for result in raw_data.results]
        return [movies, raw_data.total_pages, raw_data.page]
    else:
        return None


def movie_details(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{movie_id}?'.format(movie_id=movie_id)
    raw_data = json_responder(url)
    return DetailsMovie(raw_data.results)
