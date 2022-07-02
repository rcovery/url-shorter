from django.shortcuts import render
from django.contrib import messages
from .forms import UrlForm
from src.models import Urls
from string import hexdigits
from random import choice

def index(request):
    context = {}
    template = 'app/index.html'

    if request.method == 'POST':
        data = dict(request.POST)

        if 'name' in data and len(data['name']) > 3:
            # Check if exists
            already_exists = Urls.objects.filter(
                name = data['name']
            )

            if already_exists:
                messages.error(request, 'Este nome está indisponível!')
                return render(request, template, context)
        else:
            data['name'] = generate_url(8)

        form = UrlForm(request.POST)
        if form.is_valid():
            new_url = Urls.objects.create(
                name = data['name'],
                url = data['url']
            )

            messages.info(request, 'URL criada!')

            context['name'] = data['name']
            context['url'] = data['url']
        else:
            messages.error(request, 'Preencha corretamente os dados do formulário!')

    return render(request, template, context)

def generate_url(length):
    return ''.join(choice(hexdigits) for i in range(length))