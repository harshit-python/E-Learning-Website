from django.shortcuts import render
from .models import Tutorial, Quiz, MockTest

def home(request):
    return render(request, "home.html")

def quiz(request):
    quizzes = Quiz.objects.all()
    return render(request, "quiz.html", {"quizzes":quizzes})

def tutorials(request):
    tutorials = Tutorial.objects.all()
    return render(request, "tutorials.html",{"tutorials": tutorials})

def mocktests(request):
    tests = MockTest.objects.all()
    return render(request, "mocktests.html", {"tests":tests})

def contact(request):
    return render(request, "contact.html")




