from django.shortcuts import render
from django.contrib import messages
from .forms import UrlForm
from src.models import Urls

def index(request):
    context = {}
    template = 'app/index.html'

    if request.method == 'POST':
        data = dict(request.POST)

        if 'name' in data:
            # Check if exists
            already_exists = Urls.objects.filter(
                name = data['name']
            )

            if already_exists:
                messages.error(request, 'Este nome está indisponível!')
                return render(request, template, context)
        else:
            data['name'] = '8a3i93paldIAjw0'

        form = UrlForm(request.POST)
        if form.is_valid():
            new_url = Urls.objects.create(
                name = data['name'],
                url = data['url']
            )

            messages.info(request, 'URL criada!')
        else:
            messages.error(request, 'Preencha corretamente os dados do formulário!')

    return render(request, template, context)
