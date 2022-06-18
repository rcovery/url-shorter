from django.shortcuts import render
from .forms import UserForm

def index(request):
    return render(request, 'app/index.html', { 'id': 5 })

def login(request):
    return render(request, 'app/login.html')

def create(request):
    template = 'app/create.html'
    context = {}

    form = UserForm(request.POST or None)
    if (request.POST):
        form.save()
        template = 'app/login.html'
    else:
        context['form'] = form

    return render(request, template, context)
