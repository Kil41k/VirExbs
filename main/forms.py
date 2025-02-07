from django import forms
from .models import Articles, Comment

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
    category = forms.Select(attrs={
        'class': 'form-select bg-light', 'placeholder': 'Категория'
    })
    class Meta:
        model = Articles
        fields = ['name', 'image', 'category', 'description']

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Leave a comment...'
    }))
    class Meta:
        model = Comment
        fields = ['text']