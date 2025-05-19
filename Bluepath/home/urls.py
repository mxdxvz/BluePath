from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('after_login/', views.after_login_view, name='after_login'),
    path('signup/', views.signup_view, name='signup'),
    path('directory/', views.directory_view, name='directory'),
    path('map/', views.map_view, name='map'),
    path('help/', views.help_view, name='help'),
    path('features/', views.features_view, name='features'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('notification/', views.notification_view, name='notification'),
    path('saved/', views.saved_view, name='saved'),
    path('settings/', views.settings_view, name='settings'),
    path('phelan/', views.phelan_view, name='phelan'),
    path('santos/', views.santos_view, name='santos'),
    path('tour/', views.tour_view, name='tour'),
]
