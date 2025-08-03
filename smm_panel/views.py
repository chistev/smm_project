from django.shortcuts import render

def home(request):
    return render(request, 'smm_panel/index.html')

def signup(request):
    return render(request, 'smm_panel/signup.html')

def login(request):
    return render(request, 'smm_panel/login.html')
