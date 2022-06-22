from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index, name="index")
]

# Criar teste para url e view, após criar o teste, começar a criar as rotinas...
