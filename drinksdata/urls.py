from django.urls import path
from .views import drink_list

urlpatterns = [
    
    path('', drink_list, name = 'drinks-list'),
]