from django.urls import path

from . import views

APP_NAME = 'listen'

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('nature/', views.nature, name='nature'),
  path('office/', views.office, name='office'),
  path('public/', views.public, name='public'),
]
