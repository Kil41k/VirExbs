from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Название'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Описание'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control', 'placeholder': 'Вставьте изображение для выставки'
    }))
    class Meta:
        model = Articles
        fields = ['name', 'image', 'category', 'description']