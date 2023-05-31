from django.db import models

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

# Create your models here.
class Penguin(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} ({self.id})'

class Feeding(models.Model):
    date = models.DateField()
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

    def __str(self):
        return f'{self.get_meal_display()} on {self.date} is {self.get_food_display()}'