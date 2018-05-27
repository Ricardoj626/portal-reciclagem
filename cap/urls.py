from django.conf.urls import url
from .views import Cap_View, Observacoes_View

urlpatterns = [
    url(r"<int:pk>/obs/", Observacoes_View, name="observacoes"),
    url(r"^$", Cap_View.as_view(), name="cap"),

]