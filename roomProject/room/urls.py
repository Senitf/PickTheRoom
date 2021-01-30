from django.urls import path
from room import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search')
]