from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('', drink_list, name = 'drinks-list'),
    path("<int:id>", drink_detail, name = "single-drink"),

]

urlpatterns = format_suffix_patterns(urlpatterns)