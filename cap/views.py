import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View
from .models import Ocorrencia, Observacoes


class Cap_View(View):
    def get(self, request, *args, **kwargs):
        ocorrencia = Ocorrencia.objects.all()

        context = {
            "ocorrencias": ocorrencia,
        }
        return render(request, 'cap/cap.html', context)



# class Observacoes_View(View):
#     def get(self, request, *args, **kwargs):
#         print('agora vai')
#         ocorrencia = get_object_or_404(Ocorrencia, pk=3)
#         observacoes = Observacoes.objects.filter(ocorrencia=3)
#
#         context = {
#             "ocorrencia": ocorrencia,
#
#             "observacoes": observacoes,
#         }
#
#         return render(request, 'cap/cap.html', context)


def Observacoes_View(request, pk):
    # ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    ocorrencia = Ocorrencia.objects.all()
    print(ocorrencia)

    observacoes = Observacoes.objects.filter(ocorrencia=pk)
    print(observacoes)

    params = {
        "ocorrencia": ocorrencia,

        "observacoes": observacoes,
    }


    return HttpResponse(params)