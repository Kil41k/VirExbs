from django.db import models

class ArticleCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class Articles(models.Model):
    image = models.ImageField(upload_to='Exhibition_image')
    name = models.CharField("введите название выставки",max_length=125)
    description = models.TextField('описание фотографии', blank=True, null=True)
    image_1 = models.ImageField(upload_to='Exhibition_image', blank=True, null=True)
    description_1 = models.TextField('описание фотографии', blank=True, null=True)
    image_2 = models.ImageField(upload_to='Exhibition_image', blank=True, null=True)
    description_2 = models.TextField('описание фотографии', blank=True, null=True)
    image_3 = models.ImageField(upload_to='Exhibition_image', blank=True, null=True)
    description_3 = models.TextField('описание фотографии', blank=True, null=True)
    image_4 = models.ImageField(upload_to='Exhibition_image', blank=True, null=True)
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/exhibition/{self.id}'

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
