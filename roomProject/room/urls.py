from django.urls import path
from room import views

app_name = "room"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('scrap/<int:pk>/', views.Scrap.as_view(), name='scrap'),
    path('scraplist/', views.ScrapListView.as_view(), name='scraplist'),
    path('roomlist/', views.RoomListView.as_view(), name='roomlist'),
    path('crawler/', views.Crawler.as_view(), name='crawler'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)