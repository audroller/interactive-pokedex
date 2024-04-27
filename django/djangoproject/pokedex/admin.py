from django.contrib import admin

# Register your models here.
from .models import Pokemon, EleType, Ability, User, PokemonImage

admin.site.register(Pokemon)
admin.site.register(PokemonImage)
admin.site.register(EleType)
admin.site.register(Ability)
admin.site.register(User)