from django.urls import path
from .views import ClientesView, ClienteDetalleView, GenerarRutas

urlpatterns = [
    path('cliente/', ClientesView.as_view(), name='clientes_lista'),
    path('cliente/<str:pk>/', ClienteDetalleView.as_view(), name='cliente'),
    path('ruta/', GenerarRutas.as_view(), name='ruta')
]