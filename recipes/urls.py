from django.urls import path

from recipes.views import home

# Criação dos caminhos do site (As páginas)
urlpatterns = [
    path('', home),  # Home     
]
