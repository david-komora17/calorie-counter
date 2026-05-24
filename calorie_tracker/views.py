from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    """
    Main view to display all food items and total calories for today
    """
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.date_added = today
            food_item.save()
            messages.success(request, f'{food_item.name} added successfully!')
            return redirect('index')
    else:
        form = FoodItemForm()
    
    context = {
        'food_items': food_items,
        'total_calories': total_calories,
        'form': form,
    }
    return render(request, 'calorie_tracker/index.html', context)

def remove_food_item(request, item_id):
    """
    Remove a specific food item
    """
    food_item = get_object_or_404(FoodItem, id=item_id)
    if request.method == 'POST':
        item_name = food_item.name
        food_item.delete()
        messages.success(request, f'{item_name} removed successfully!')
    return redirect('index')

def reset_day(request):
    """
    Reset all food items for the current day
    """
    if request.method == 'POST':
        today = timezone.now().date()
        deleted_count, _ = FoodItem.objects.filter(date_added=today).delete()
        messages.success(request, f'Reset completed! Removed {deleted_count} items.')
    return redirect('index')