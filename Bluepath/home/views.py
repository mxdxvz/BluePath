# views.py

from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')  # or your template file

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def directory_view(request):
    return render(request, 'directory.html')

def map_view(request):
    return render(request, 'map.html')
    
def help_view(request):
    return render(request, 'help.html')

def features_view(request):
    return render(request, 'features.html')

def feedback_view(request):
    return render(request, 'feedback.html')

def notification_view(request):
    return render(request, 'notification.html')

def saved_view(request):
    return render(request, 'saved.html')

def settings_view(request):
    return render(request, 'settings.html')

def phelan_view(request):
    return render(request, 'phelan.html')

def santos_view(request):
    return render(request, 'santos.html')

def after_login_view(request):
    return render(request, 'after_login.html')



