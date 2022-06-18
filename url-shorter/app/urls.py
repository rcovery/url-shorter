from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('create/', views.create, name="create")
]
