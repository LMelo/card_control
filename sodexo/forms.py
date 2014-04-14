#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms
from models import Restaurant


class MealForm(forms.Form):
    value = forms.DecimalField(decimal_places=2)
    date = forms.DateField()
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all(), label='Restaurant', required=False)