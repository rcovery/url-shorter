from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<url_name>', views.track, name="track"),
]
