from django.shortcuts import render
from . import ml_model

def home(request):
    return render(request, 'index.html')

def result(request):
    user_input = request.GET['user_input']
    user_input = ml_model.multiplier(user_input)
    return render(request, 'result.html', {'home_input':user_input})