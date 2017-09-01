from django.conf.urls import url
from . import views

app_name = 'movie'

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^search/$', views.search_view, name='search'),
    url(r'^account/', views.account_view, name='account'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_view, name='movie'),
    url(r'^like/(?P<movie_id>[0-9]+)/$', views.like_movie, name='like'),
    url(r'^dislike/(?P<movie_id>[0-9]+)/$', views.dislike_movie, name='dislike')
]
