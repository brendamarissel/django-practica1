from django.contrib import admin
from django.urls import path
from app_web.views import index, editar_persona, eliminar_persona

urlpatterns = [
    path("", index, name="index"),
    path("editar/<int:id>/", editar_persona, name="editar"),
    path("eliminar/<int:id>/", eliminar_persona, name="eliminar"),
]