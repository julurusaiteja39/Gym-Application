from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('excercise/', views.excercise, name='excercise'),
    path('nutrition/', views.nutrition, name='nutrition'),
    # path('register/', views.register, name='blog-register'),

]