from django.urls import path
from . import views

#namespace
app_name = "news"
urlpatterns = [
    #function base view
    path('', views.indexClass.as_view(), name='index'),
    #path('add/',views.add_post, name='add'),
    path('save/',views.save_news_class.as_view(), name='save'),
    path('email/',views.sendEmail, name='email'),
    path('print/',views.printEmail, name='print'),
]