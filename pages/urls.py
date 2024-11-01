
from django.urls import path
from . import views

urlpatterns = [
    # Root URL
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
