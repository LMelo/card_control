from django.shortcuts import render
from forms import MealForm
from models import Meal


def restaurante_new(request):
    return render(request, 'restaurant_new.html')


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