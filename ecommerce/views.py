from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Nave

# Create your views here.
def home(request):
    naves = list(Nave.objects.values())
    if naves:
        return JsonResponse(naves, safe=False)
    # else:
    #     return HttpResponse(f"No hay naves 123 {naves}")

def nave(request, id):
    task = Nave.objects.get(id=id)
    return HttpResponse("nave: %s" % task.marca)