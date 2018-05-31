from django.contrib import admin
from .models import Empresa, Estoque, Fabrica, Funcionario, Produto
# Register your models here.


class FabricaInline(admin.StackedInline):
    model = Fabrica
    extra = 0

class EstoqueInline(admin.TabularInline):
    model = Estoque
    extra = 0




class EmpresaAdmin(admin.ModelAdmin):
    inlines = (FabricaInline,)

    list_display = ("nome", "cnpj", "categoria", "data_criacao")
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             ('nome',
    #             'data_nascimento'),
    #         )
    #     }),
    #
    #
    # )
    # ordering = ["-data_notificacao"]
    # search_fields = ("nome", "municipio_residencia", "bairro", "telefone")
    # list_filter = ("nome", "bairro")
    date_hierarchy = 'ultima_atualizacao'



class FabricaAdmin(admin.ModelAdmin):
    inlines = (EstoqueInline,)

    list_display = ("empresa", "endereco", "categoria", "ultima_atualizacao")
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             ('nome',
    #             'data_nascimento'),
    #         )
    #     }),
    #
    #
    # )
    # ordering = ["-data_notificacao"]
    # search_fields = ("nome", "municipio_residencia", "bairro", "telefone")
    # list_filter = ("nome", "bairro")
    date_hierarchy = 'ultima_atualizacao'


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(Funcionario)
