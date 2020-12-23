from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('quiz', views.quiz, name="quiz"),
    path('tutorials', views.tutorials, name="tutorials"),
    path('mocktests', views.mocktests, name="mocktests"),
    path('contact', views.contact, name="contact"),

]