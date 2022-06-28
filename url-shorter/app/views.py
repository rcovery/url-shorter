from django.shortcuts import render
from .forms import UrlForm
from src.models import Urls

def index(request):
    context = {}
    template = 'app/index.html'
    
    if request.method == 'GET':
        context['form'] = UrlForm()

    elif request.method == 'POST':
        context = dict(request.POST)

        if 'name' in context:
            # Check if exists
            already_exists = Urls.objects.filter(
                name = context['name']
            )

            if already_exists:
                return render(request, 'app/404.html', context)
        else:
            context['name'] = '8a3i93paldIAjw0'

        form = UrlForm(context)
        if form.is_valid():
            new_url = Urls.objects.create(
                name = context['name'],
                url = context['url']
            )

    return render(request, template, context)
