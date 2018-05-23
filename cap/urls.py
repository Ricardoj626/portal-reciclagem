from django.conf.urls import url
from .views import Cap_View

urlpatterns = [
    url(r"^$", Cap_View.as_view(), name="cap"),

    ]