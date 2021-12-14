
from django.urls import path

from . import views

app_name = 'react_demo_django_app'
urlpatterns = [
    path('home/', views.home, name='home'),
]
