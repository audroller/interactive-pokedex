from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemon

# Create your views here.

def index(request):
    return render(request, "index.html", { "pokemon": Pokemon.objects.order_by("number").all() })