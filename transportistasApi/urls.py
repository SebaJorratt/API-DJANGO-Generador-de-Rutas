from django.urls import path
from .views import TransportistaDetalleView, TransportistaView, numero

urlpatterns = [
    path('transportista/', TransportistaView.as_view(), name='transportista_lista'),
    path('transportista/<str:pk>/', TransportistaDetalleView.as_view(), name='transportista'),
    path('numero/', numero.as_view(), name='numero')
]