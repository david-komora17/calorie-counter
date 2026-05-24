from django.db import models
from django.utils import timezone

# Create your models here.
class FoodItem (models.Model):
    """
    Model representing a food item with its calorie count.
    """
    name = models.CharField(max_length=200, help_text ="Name of the food item...")
    calories = models.IntegerField(help_text="Calorie count per serving")
    date_added = models.DateField(default=timezone.now, help_text="Date when foo was added")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.calories} calories"