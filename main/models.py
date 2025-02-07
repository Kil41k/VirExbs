from django.db import models
from users.models import User

class ArticleCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class Articles(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.FileField()
    name = models.CharField(max_length=125)
    description = models.TextField()
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/exhibition/{self.id}'

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'

class Comment(models.Model):
    article = models.ForeignKey(to=Articles, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)