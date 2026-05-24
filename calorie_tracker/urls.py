from django.urls import path
from . import views

app_name = 'calorie_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<int:item_id>/', views.remove_food_item, name='remove'),
    path('reset/', views.reset_day, name='reset'),
]