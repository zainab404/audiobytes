from django.urls import path

from . import views

APP_NAME = 'listen'

urlpatterns = [
  path('', views.index, name='index'),
]
