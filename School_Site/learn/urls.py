from django.urls import path
from . import views

APP_NAME = 'learn'
URL_PATTERNS = [
    path('', views.home, name = 'Home'),
    path('Subjects/', views.subjects, name = 'Subjects'),
    path('Profile/',views.userprofile, name = 'Profile'),
    path('Resources/', views.resources, name = 'Resources'),
    path('News/', views.news, name = 'News'),
    path('Progress/', views.progress, name = 'Progress'),
    path('CreatePlan/', views.createplan, name = 'CreatePlan'),
    path('', views.v, name = ''),
    path('', views.v, name = ''),
    path('', views.v, name = ''),
    path('', views.v, name = ''),
    path('', views.v, name = ''),
    path('', views.v, name = ''),
    path('', views.v, name = ''),
]