#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'sodexo.views',
    url(r'^restaurant/$', 'restaurant_index', name="restaurant_list"),
    url(r'^restaurant_new/$', 'restaurant_new', name="restaurant_new"),
    url(r'^meal_new/$', 'meal_new'),
    url(r'^meal_list/$', 'meal_index'),
)


