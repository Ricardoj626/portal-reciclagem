from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import Ocorrencia, Vitima, Agressor


class Policia_View(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        vitimas = Vitima.objects.all()
        agressores = Agressor.objects.all()
        context = {
            "ocorrencias": ocorrencias,
            "vitimas": vitimas,
            "agressores": agressores,
        }
        return render(request, 'policia_militar/pm.html', context)