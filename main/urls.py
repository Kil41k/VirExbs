from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import index, exhibitions, create, exhibition_detail, exhibition_edit, exhibition_delete

app_name = 'articles'

urlpatterns = [
    path('', index, name='home'),
    path('exhibitions/', exhibitions, name='exhibitions'),
    path('exhibitions/category/<int:category_id>/', exhibitions, name='category'),
    path('create/', create, name='create'),
    path('exhibition/<int:id>/', exhibition_detail, name='exhibition_detail'),
    path('exhibition/<int:id>/edit/', exhibition_edit, name='exhibition_edit'),
    path('exhibition/<int:id>/delete/', exhibition_delete, name='exhibition_delete'),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)