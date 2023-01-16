from django.views import View
from .models import Transportista
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from clientesApi.solucion import algoritmo

class TransportistaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        lista = Transportista.objects.all()
        return JsonResponse(list(lista.values()), safe = False)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        if jd['codigo'] != "":
            Transportista.objects.create(
                codigo=jd['codigo'],
                nombre=jd['nombre'],
                numero=jd['numero'],
            )
            datos={'message':"Se cargaron los datos satisfactoriamente!"}
        else:
            datos={'message':"No se ha logrado crear al transportista"}
        return JsonResponse(datos)

class TransportistaDetalleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        transportista = Transportista.objects.get(pk = pk)
        return JsonResponse(model_to_dict(transportista))

    def put(self, request, pk=0):
        jd=json.loads(request.body)
        transportistas = list(Transportista.objects.filter(pk = pk).values())
        if len(transportistas) > 0:
            transportista=Transportista.objects.get(pk = pk)
            transportista.nombre=jd['nombre']
            transportista.save()
            datos = {'mesage':"Transportista modificado satisfactoriamente"}
        else:
            datos = {'message':"Transportista no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, pk=0):
        transportistas = list(Transportista.objects.filter(pk = pk).values())
        if len(transportistas) > 0:
            Transportista.objects.filter(pk = pk).delete()
            datos = {'message' : "Transportista eliminado satisfactoriamente!"}
        else:
            datos = {'message' : "Transportista no encontrado"}
        return JsonResponse(datos)

class numero(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        lista = Transportista.objects.all()
        mayor = self.obtenerMayor(lista)
        datos = {'valor' : mayor+1}
        return JsonResponse(datos)
    
    def obtenerMayor(self, lista):
        mayor = 0
        for i in lista:
            if i.numero > mayor:
                mayor = i.numero
        return mayor