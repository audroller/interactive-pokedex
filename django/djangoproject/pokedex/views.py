from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemon

# Create your views here.

def index(request):
    return get_pokemon(request, 1)

def get_pokemon(request, pokemon_number):
    return render(request, "index.html", { "selected_pokemon": Pokemon.objects.get(number=pokemon_number), "pokemon": Pokemon.objects.order_by("number").all() })