from django.urls import path
from room import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search')
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)