from django import forms 
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    """
    Form for adding and validating new food items.
    """
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-200 bg-gray-50 focus:bg-white text-gray-800',
                'placeholder': 'e.g., Avocado Toast'
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-200 bg-gray-50 focus:bg-white text-gray-800',
                'placeholder': 'e.g., 350'
            }),
        }

    def clean_calories(self):
        """
        Validates that calories are a realistic positive integer.
        """
        calories = self.cleaned_data.get('calories')
        if calories is None or calories <= 0:
            raise forms.ValidationError('Calories must be a positive number greater than 0.')
        if calories > 5000:
            raise forms.ValidationError('Surely nothing you ate in one sitting is over 5,000 calories!')
        return calories