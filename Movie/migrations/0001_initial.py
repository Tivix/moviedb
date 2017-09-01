# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 11:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=150)),
                ('year', models.IntegerField(default=0)),
                ('cover_url', models.CharField(max_length=400)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movie.Movie'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
