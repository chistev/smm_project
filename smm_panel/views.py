from django.shortcuts import render

def home(request):
    return render(request, 'smm_panel/index.html')

def signup(request):
    return render(request, 'smm_panel/signup.html')

def login(request):
    return render(request, 'smm_panel/login.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # TODO: Add password reset logic here (e.g., send reset link)
        return render(request, 'smm_panel/forgot_password.html', {'message': 'If the email exists, a reset link has been sent.'})
    return render(request, 'smm_panel/forgot_password.html')
