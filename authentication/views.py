from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm


def home(request):
    return render(request, 'authentication/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            #if you want user to get logged in after sign up 
            #user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', { 'form' : form })