from django.shortcuts import render
from .forms import UrlForm

def index(request):
    return render(request, 'app/index.html')
