from django.shortcuts import render
from django.contrib import messages
from .forms import UrlForm
from src.models import Urls

def index(request):
    context = {}
    template = 'app/index.html'

    if request.method == 'POST':
        context = dict(request.POST)

        if 'name' in context:
            # Check if exists
            already_exists = Urls.objects.filter(
                name = context['name']
            )

            if already_exists:
                messages.error(request, 'Este nome está indisponível!')
                return render(request, template, context)
        else:
            context['name'] = '8a3i93paldIAjw0'

        form = UrlForm(context)
        if form.is_valid():
            new_url = Urls.objects.create(
                name = context['name'],
                url = context['url']
            )

            messages.info(request, 'Nova URL copiada!')

    return render(request, template, context)
