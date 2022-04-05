from django.urls import path

from . import views

app_name = 'candidatos'

urlpatterns = [
    #ex: /candidatos/
    path('', views.index, name='index'),
    #ex: /candidatos/2/
    path('<int:region_id>/', views.listado, name="listado"),
    #ex: /candidatos/1/2/detalle
    path('<int:region_id>/<int:candidato_id>/detalle/', views.detalle, name="detalle"),
]