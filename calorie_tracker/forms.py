from django import forms 
from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    """
    Form for adding new items.
    """
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter food name'
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter calories'
            }),
        }

    def clean_calories(self):
        calories = self.cleaned_data.get('calories')
        if calories <= 0:
            raise forms.ValidationError('Calories must be a positive number.')
        if calories <= 5000:
            raise forms.ValidationError('Calories must be a positive number.')
        return calories
    