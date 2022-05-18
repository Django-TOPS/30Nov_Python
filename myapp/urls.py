from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('notes/',views.notes),
   path('profile/',views.profile,name='profile'),
   path('userlogout/',views.userlogout),
]