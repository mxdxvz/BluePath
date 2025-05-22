from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            # Authenticate and log in the user
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            messages.success(request, f'Welcome, {username}! You are now logged in.')
            return redirect('home')  # Redirects to the home view below
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


@login_required
def home(request):
    return render(request, 'after_login.html')