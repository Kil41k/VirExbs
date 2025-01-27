from django.contrib import admin
from .models import Articles, ArticleCategory

admin.site.register(Articles)
admin.site.register(ArticleCategory)