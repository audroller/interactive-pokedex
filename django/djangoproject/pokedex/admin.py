from django.contrib import admin

# Register your models here.
from .models import Pokemon, EleType, Ability

admin.site.register(Pokemon)
admin.site.register(EleType)
admin.site.register(Ability)
