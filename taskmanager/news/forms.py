from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'is_featured', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-3 rounded-lg bg-gray-100 dark:bg-dark-border text-gray-800 dark:text-dark-text'}),
            'anons': forms.Textarea(attrs={'class': 'w-full p-3 rounded-lg bg-gray-100 dark:bg-dark-border text-gray-800 dark:text-dark-text', 'rows': 3}),
            'full_text': forms.Textarea(attrs={'class': 'w-full p-3 rounded-lg bg-gray-100 dark:bg-dark-border text-gray-800 dark:text-dark-text', 'rows': 10}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'w-5 h-5'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-3 rounded-lg bg-gray-100 dark:bg-dark-border text-gray-800 dark:text-dark-text'}),
        }