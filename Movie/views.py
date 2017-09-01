# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import datetime
from models import *
from django.db.models import Q
from . import context_builders
import helpers

def home_view(request):
    template = 'home_page.html'
    context = context_builders.home_page_context(request)

    return render(request, template, context)

def search_view(request):
    template = 'search_page.html'
    page_context = context_builders.search_page_context(request)
    if page_context:
        context = {
            'movies': page_context[0],
            'counter': page_context[1],
            'page': page_context[2],
            'next_page': page_context[2] + 1,
            'prev_page': page_context[2] - 1,
            'start_row': [1, 5, 9, 13, 17],
            'end_row': [4, 8, 12, 16, 20]
        }
    else:
        context ={
            'error': True
        }
    return render(request, template, context)

def movie_view(request, movie_id):
    template = 'movie_page.html'
    context = context_builders.movie_page_context(request, movie_id)
    return render(request, template, context)

def account_view(request):
    template = 'account_page.html'

    if request.user.is_authenticated():
        context = {
            'movies': request.user.like_set.all(),
        }
        return render(request, template, context)
    return home_view(request)


def like_movie(request, movie_id):
    if request.user.is_authenticated():
        #Check is already exist
        movie = Movie.objects.filter(movie_id=movie_id).first()
        if not movie:
            movie = helpers.add_movie_to_db(movie_id)
        #Check is not liked
        like = Like.objects.filter(movie=movie,user=request.user)
        if not like:
            like = Like(
                movie=movie,
                user=request.user,
            )
            like.save()
    return movie_view(request, movie_id)

def dislike_movie(request, movie_id):
    if request.user.is_authenticated:
        movie = Movie.objects.filter(movie_id=movie_id)
        like = Like.objects.filter(movie=movie, user=request.user)
        like.delete()
    return movie_view(request, movie_id)

def login_view(request):
    template = 'login_page.html'

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return home_view(request)
        return render(request, template)
    return render(request, template)


def logout_view(request):
    logout(request)
    return home_view(request)


def register_view(request):
    if request.method == "POST":
        username = request.POST['register_username']
        password = request.POST['register_password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.filter(username=username)
        if not user:
            if password == confirm_password:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return home_view(request)
    return render(request, 'login_page.html')
