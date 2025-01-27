from django.forms import ModelForm, TextInput
from .models import Articles

class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['name', 'image', 'category', 'description', 'description_1', 'description_2', 'description_3', 'image_1',
                  'image_2','image_3','image_4']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'description': TextInput(attrs={
                'placeholder': 'Описание'
            }),
            'description_1': TextInput(attrs={
                'placeholder': 'Описание'
            }),
            'description_2': TextInput(attrs={
                'placeholder': 'Описание'
            }),
            'description_3': TextInput(attrs={
                'placeholder': 'Описание'
            }),
        }