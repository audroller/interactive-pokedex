from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pokemon_number>', views.get_pokemon)
]