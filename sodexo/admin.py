from django.contrib import admin
from models import Restaurant, Meal


class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_restaurant', 'meal_date', 'meal_value')

admin.site.register(Restaurant)
admin.site.register(Meal, MealAdmin)
