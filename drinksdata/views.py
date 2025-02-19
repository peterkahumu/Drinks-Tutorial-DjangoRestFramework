from django.shortcuts import render
from django.http import JsonResponse
from .models  import Drinks
from django.views import View
from .serializers import DrinkSerializer

# Create your views here.

def drink_list(request):
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks, many=True).data

    return JsonResponse({"drinks": serializer})


