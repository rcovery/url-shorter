from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from src.models import Urls
from .forms import UrlForm
from string import hexdigits
from random import choice
from urllib.parse import quote

import requests

def index(request):
    context = {}
    template = 'app/index.html'

    if request.method == 'POST':
        data = {}
        post = request.POST

        if 'name' in post and len(post['name']) > 3:
            # Check if exists
            data['name'] = parse_name(post['name'])

            already_exists = Urls.objects.filter(
                name = data['name']
            )

            if already_exists:
                messages.error(request, 'Este nome está indisponível!')
                return render(request, template, context)
        else:
            data['name'] = generate_url(8)

        form = UrlForm(post)
        if form.is_valid() and 'localhost' not in post['url'] and '127.0.0.1' not in post['url']:
            try:
                url_response = requests.get(post['url'], timeout=3)
            except requests.exceptions.Timeout:
                messages.error(request, 'Esta URL não está respondendo!')
                return render(request, template, context)

            if (url_response.status_code >= 400):
                messages.error(request, 'Esta URL não está correta!')
                return render(request, template, context)

            new_url = Urls.objects.create(
                name = data['name'],
                url = post['url']
            )

            messages.info(request, 'Sua URL foi criada e copiada!')

            context['name'] = data['name']
            context['full_url'] = request.build_absolute_uri() + data['name']
        else:
            messages.error(request, 'Preencha corretamente os dados do formulário!')

    return render(request, template, context)

def track(request, url_name):
    context = {}
    template = 'app/404.html'

    try:
        exists = Urls.objects.get(
            name = url_name
        )

        if exists:
            return redirect(exists.url)
    except:
        pass

    return render(request, template, context)

def generate_url(length):
    return ''.join(choice(hexdigits) for i in range(length))

def parse_name(data):
    return quote(data.strip().lower().replace(' ', '_'))