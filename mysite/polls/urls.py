from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls'),
    path('list/',views.viewList, name='list'),
    path('detail/<int:question_id>/',views.viewDetail, name ='detail'),
    path('<int:question_id>',views.vote, name='vote'),
]