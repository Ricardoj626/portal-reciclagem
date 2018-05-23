from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import Ocorrencia


class Cap_View(View):
    def get(self, request, *args, **kwargs):
        ocorrencia = Ocorrencia.objects.all()

        context = {
            "ocorrencias": ocorrencia,
        }
        return render(request, 'cap/cap.html', context)