from django.urls import path,register_converter
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('',views.home,name = 'homepage'),
    path('search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
