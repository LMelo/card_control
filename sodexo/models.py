from django.db import models
from datetime import date


class Restaurant(models.Model):
    rest_name = models.CharField(verbose_name="name", max_length=100)


class Meal(models.Model):
    meal_value = models.DecimalField(verbose_name="value", max_digits=10, decimal_places=2)
    meal_date = models.DateField(verbose_name="date", auto_now_add=True, default=date.today())
    meal_restaurant = models.ForeignKey(
        to=Restaurant, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="restaurant"
    )

    def __unicode__(self):
        return '%s - %s: R$ %s' % (self.meal_date, self.meal_restaurant or '', self.meal_value)
