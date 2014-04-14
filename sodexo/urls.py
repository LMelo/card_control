#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'sodexo.views',
    url(r'^restaurant_new/$', 'restaurante_new'),
    url(r'^meal_new/$', 'meal_new'),
    url(r'^meal_list/$', 'meal_index'),
)


