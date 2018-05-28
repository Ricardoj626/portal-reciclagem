from django.conf.urls import url
from django.urls import path

from .views import Cap_View, Observacoes_View

urlpatterns = [
    path(r"<int:pk>/obs/", Observacoes_View, name="observacoes"),
    path(r"", Cap_View.as_view(), name="cap"),

]