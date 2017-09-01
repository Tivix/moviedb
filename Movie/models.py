# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=150)
    cover_url = models.CharField(max_length=400)
    rating = models.DecimalField(max_digits=4, decimal_places=1)

class Like(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
