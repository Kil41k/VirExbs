from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ExhibitionsView.as_view(), name='home'),
    path('category/<int:category_id>/', views.ExhibitionsView.as_view(), name='category'),
    path('create/', views.ExbCreateView.as_view(), name='create'),
    path('<int:id>/', views.exhibition_detail, name='exhibition_detail'),
    path('<int:id>/edit/', views.exhibition_edit, name='exhibition_edit'),
    path('<int:id>/delete/', views.exhibition_delete, name='exhibition_delete'),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)