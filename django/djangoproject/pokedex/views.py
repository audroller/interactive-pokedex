from django.http import HttpResponse
from django.shortcuts import render

from django.db.models.functions import Length

from .models import Pokemon

# Create your views here.

def index(request):
    return get_pokemon(request, 1)

def get_pokemon(request, pokemon_number):
    selected_pokemon = Pokemon.objects.get(number=pokemon_number)

    return render(request, "index.html", { 
        "selected_pokemon": selected_pokemon, 
        "selected_pokemon_images": selected_pokemon.pokemonimage_set.order_by(Length('description').asc()).all(),
        "selected_pokemon_types": selected_pokemon.type.all(),
        "selected_pokemon_abilities": selected_pokemon.abilities.all(),
        "selected_pokemon_postevolutions": selected_pokemon.postevolutions.all(),
        "pokemon": Pokemon.objects.order_by("number").all() 
    })