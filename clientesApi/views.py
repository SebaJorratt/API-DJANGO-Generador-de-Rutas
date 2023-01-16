from django.views import View
from .models import Cliente
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from clientesApi.solucion import algoritmo
from clientesApi.pandas import importar

class ClientesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        lista = Cliente.objects.all()
        return JsonResponse(list(lista.values()), safe = False)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        if jd['codigo'] != "":
            Cliente.objects.create(
                codigo=jd['codigo'],
                nombre=jd['nombre'],
                dias=jd['dias'],
                longitud=jd['longitud'],
                latitud=jd['latitud'],
                tipo=jd['tipo'],
                sector=jd['sector'],
                zona=jd['zona'],
                direccion=jd['direccion']
            )
            datos={'message':"Se cargaron los datos satisfactoriamente!"}
        else:
            datos={'message':"No se ha logrado crear al cliente"}
        return JsonResponse(datos)

class ClienteDetalleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        cliente = Cliente.objects.get(pk = pk)
        return JsonResponse(model_to_dict(cliente))

    def put(self, request, pk=0):
        jd=json.loads(request.body)
        clientes = list(Cliente.objects.filter(pk = pk).values())
        if len(clientes) > 0:
            cliente=Cliente.objects.get(pk = pk)
            cliente.nombre=jd['nombre']
            cliente.dias=jd['dias']
            cliente.longitud=jd['longitud']
            cliente.latitud=jd['latitud']
            cliente.tipo=jd['tipo']
            cliente.sector=jd['sector']
            cliente.zona=jd['zona']
            cliente.direccion=jd['direccion']
            cliente.save()
            datos = {'mesage':"Cliente modificado satisfactoriamente"}
        else:
            datos = {'message':"Cliente no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, pk=0):
        clientes = list(Cliente.objects.filter(pk = pk).values())
        if len(clientes) > 0:
            Cliente.objects.filter(pk = pk).delete()
            datos = {'message' : "Cliente eliminado satisfactoriamente!"}
        else:
            datos = {'message' : "Cliente no encontrado"}
        return JsonResponse(datos)

class GenerarRutas(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        jd=json.loads(request.body)
        resultado = algoritmo(jd)
        tiempos = []
        for i in range(len(resultado)):
            tiempo = 0
            for j in range(len(resultado[i])):
                if jd[resultado[i][j]]['tipo'] == "Supermercados":
                   tiempo = tiempo + 120
                elif jd[resultado[i][j]]['tipo'] == "sucursal":
                    tiempo = tiempo + 0
                else:
                    tiempo = tiempo + 12
            tiempos.append(tiempo)
        datos = {'resultado':resultado, 'tiempos':tiempos}
        return JsonResponse(datos)

    def get(self, request):
        jd = importar()
        if jd[0]['codigo'] == 1:
            for i in range(len(jd)):
                if jd[i]['codigo'] != "":
                    Cliente.objects.create(
                        codigo=jd[i]['codigo'],
                        nombre=jd[i]['nombre'],
                        dias=jd[i]['dias'],
                        longitud=jd[i]['longitud'],
                        latitud=jd[i]['latitud'],
                        tipo=jd[i]['tipo'],
                        sector=jd[i]['sector'],
                        zona=jd[i]['zona'],
                        direccion=jd[i]['direccion']
                    )
            datos={'message':"Se cargaron los datos satisfactoriamente!"}        
        else:
            datos = {'message' : "Error en el formato del archivo Excel"}
        return JsonResponse(datos)

    def put(self, request):
        jd=json.loads(request.body)
        for i in range(len(jd)):
            if jd[i]['codigo'] != "":
                Cliente.objects.create(
                    codigo=jd[i]['codigo'],
                    nombre=jd[i]['nombre'],
                    dias=jd[i]['dias'],
                    longitud=jd[i]['longitud'],
                    latitud=jd[i]['latitud'],
                    tipo=jd[i]['tipo'],
                    sector=jd[i]['sector'],
                    zona=jd[i]['zona'],
                    direccion=jd[i]['direccion']
                )
        datos={'message':"Se cargaron los datos satisfactoriamente!"}        
        return JsonResponse(datos)