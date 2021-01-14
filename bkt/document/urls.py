from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<slug:slug>',views.radarDetail, name='detail'),
    path('search/', views.searchContent, name='search'),
]