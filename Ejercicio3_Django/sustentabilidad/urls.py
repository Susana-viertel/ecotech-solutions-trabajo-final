from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('metricas/', views.metricas, name='metricas'),
    path('panel/', views.vista_panel_sustentabilidad, name='panel'),
]