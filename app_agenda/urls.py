from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarcontato/', views.registrarcontato),
    path('edicaocontato/<id>', views.edicaocontato),
    path('editarcontato/', views.editarcontato),
    path('excluircontato/<id>', views.excluircontato),
    path('cancelaredicao/', views.cancelaredicao)

]
