from django.shortcuts import render, redirect
from forms import MealForm
from models import Meal
from sodexo.forms import RestaurantForm, Restaurant


# RESTAURANT
def restaurant_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_index.html', {'object_list': restaurants})


def restaurant_new(request, *args, **kwargs):
    if request.method == 'POST':
        form_restaurant = RestaurantForm(request.POST)
        if form_restaurant.is_valid():
            name = form_restaurant.cleaned_data['name']

            restaurant = Restaurant(rest_name=name)
            restaurant.save()
            return redirect('/sodexo/restaurant')
    else:
        form_restaurant = RestaurantForm()
        return render(request, 'restaurant_new.html', {'object_form': form_restaurant})


# MEALS
def meal_new(request, *args, **kwargs):
    if request.method == 'POST':
        meal_form = MealForm(request.POST)
        if meal_form.is_valid():
            restaurant = meal_form.cleaned_data['restaurant']
            value = meal_form.cleaned_data['value']
            date = meal_form.cleaned_data['date']

            meal = Meal(meal_value=value, meal_date=date, meal_restaurant=restaurant)
            meal.save()
    else:
        meal_form = MealForm()
    return render(request, 'meal_new.html', {'meal_form': meal_form})


def meal_index(request):
    return render(request, 'meal_index.html')