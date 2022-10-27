from django.urls import path

from . import views

# Criação dos caminhos do site (As páginas)
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
