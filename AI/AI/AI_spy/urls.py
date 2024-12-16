from django.contrib import admin 
from django.urls import path
from . import views 

app_name = 'AI_spy'
urlpatterns = [
    path('', views.index_view, name='index'),  # index_view가 호출됨
]

