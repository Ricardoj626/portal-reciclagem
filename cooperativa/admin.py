from django.contrib import admin
from .models import Cooperativa, Galpao, Estoque, Produto
# Register your models here.


admin.site.register(Cooperativa)
admin.site.register(Galpao)
admin.site.register(Produto)
admin.site.register(Estoque)

admin.site.site_header = u"Painel Administrativo"
admin.site.index_title = u"Beyound"
admin.site.site_title = u"Admin"