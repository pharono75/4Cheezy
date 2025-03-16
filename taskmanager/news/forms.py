from .models import Articles
from django.forms import ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'text text-input',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'text text-input',
                'placeholder': 'Анонс статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'text text-textarea',
                'placeholder': 'Текст статьи'
            }),
        }