from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

FOODS = (
    ('F', 'Fish'),
    ('S', 'Squid'),
    ('K', 'Krill')
)

# Many to Many (M:M) - a penguin can have many hats, and a hat can be used by many penguins
class Hat(models.Model):
    type = models.CharField(max_length=25)
    color = models.CharField(max_length=15)

    def __str__(self):
        return f'A {self.color} {self.type}'
    
    def get_absolute_url(self):
        return reverse('hats_detail', kwargs={'pk': self.id})


class Penguin(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    hats = models.ManyToManyField(Hat)
    # fk linking to user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('penguins_detail', kwargs={'penguin_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        # Default value for meal is 'B' for Breakfast
        default=MEALS[0][0]
    )
    food = models.CharField(
        max_length=1,
        choices=FOODS,
        # Default value for food is 'F' for Fish
        default=FOODS[0][0]
    )
    # penguin_id Foreign Key  |  Deletes feedings if penguin is deleted
    penguin = models.ForeignKey(Penguin, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} was {self.get_food_display()} on {self.date}'
    
    class Meta:
        # Sort Feedings by date (descending order)
        ordering = ['-date']