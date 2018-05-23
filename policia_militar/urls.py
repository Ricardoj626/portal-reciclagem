from django.conf.urls import url

from .views import Policia_View

urlpatterns = [
    url(r"^$", Policia_View.as_view(), name="policia"),

    ]