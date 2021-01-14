from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('index/',views.indexClass.as_view(),name='index'),
    path('',views.loginClass.as_view(), name="login"),
    path('userpage/',views.viewUserClass.as_view(), name="userpage"),
    path('xem_sp/',views.xem_sp, name="xem_sp"),
    path('addpost/',views.addPost.as_view(), name="addpost")
]   