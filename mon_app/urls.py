from django.urls import path
from . import views

urlpatterns = [
    path('testes/', views.teste_list),
]
