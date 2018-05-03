from django.contrib import admin

# Register your models here.
from .models import Ocorrencia, Vitima, Agressor

class VitimaAdmin(admin.ModelAdmin):

    list_display = ("data_nascimento", "nome", "telefone")
    fieldsets = (
        (None, {
            'fields': (
                ('nome',
                'data_nascimento'),
                'municipio_residencia',
                'bairro',
                'logradouro',
                'telefone',
                ('idade',
                'idade_outros'),
                'raca_cor',
                'medida_protetiva',
                'deficiencia',

                'orientacao_sexual',
                'instrucao',
                'renda_individual',


            )
        }),


    )



    # ordering = ["-data_notificacao"]
    # search_fields = ("data_ocorrencia", "nome", "tipo_violencia", "encaminhamento")
    # list_filter = ("nome", "tipo_violencia", "encaminhamento")
    # date_hierarchy = 'data_notificacao'


    save_on_top = True


class OcorrenciaAdmin(admin.ModelAdmin):

    list_display = ("vitima", "autor")
    fieldsets = (
        (None, {
            'fields': (
                ('vitima',
                'periodo_fato'),
                ('ambiente_agressao',
                'ambiente_agressao_outros'),
                ('vinculo_agressor',
                'vinculo_agressor_outros'),
                'fatores_risco',
                ('periodo_relacionamento',
                'periodo_violencia',
                'filhos'),
                'autor',

                ('atendimento_medico',
                'tipo_violencia'),
                ('natureza_ocorrencia',
                'natureza_ocorrencia_outros'),
                'acompanhamento_ppdv',

                ('data_visita_autor',
                'numero_reds_autor'),
                'observacoes_visita_autor',
                ('data_visita_vitima',
                'numero_reds_vitima'),
                'observacoes_visita_vitima',

                ('data_visita_autor_medida_protetiva',
                'numero_reds_autor_medida_protetiva'),
                'observacoes_visita_autor_medida_protetiva',
                ('data_visita_vitima_medida_protetiva',
                'numero_reds_vitima_medida_protetiva'),
                'observacoes_visita_vitima_medida_protetiva'

            )
        }),
    )

    # ordering = ["-data_notificacao"]
    search_fields = ("vitima", "autor", "tipo_violencia", "natureza_ocorrencia")
    list_filter = ("vitima", "autor", "tipo_violencia")
    # date_hierarchy = 'data_notificacao'
    save_on_top = True

class AgressorAdmin(admin.ModelAdmin):
    list_display = ("nome_autor", "rg_autor", "autor_foi_preso")
    fieldsets = (
        (None, {
            'fields': (
                'nome_autor',
                'rg_autor',
                'autor_foi_preso',
                ('autor_doenca_psicologica',
                'autor_necessita_atendimento_psicologica'),
                ('autor_suicidio',
                'autor_arma')
            )
        }),
    )

    # ordering = ["-data_notificacao"]
    search_fields = ("nome_autor", "rg_autor")
    list_filter = ("nome_autor", "autor_foi_preso")
    # date_hierarchy = 'data_notificacao'








admin.site.register(Agressor, AgressorAdmin)
admin.site.register(Vitima, VitimaAdmin)
admin.site.register(Ocorrencia, OcorrenciaAdmin)