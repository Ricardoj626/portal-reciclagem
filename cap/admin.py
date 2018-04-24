from django.contrib import admin
from .models import Ocorrencia
# Register your models here.

class OcorrenciaAdmin(admin.ModelAdmin):

    list_display = ("data_ocorrencia", "nome", "tipo_violencia", "encaminhamento")
    fieldsets = (
        (None, {
            'fields': (
                ('data_ocorrencia',
                'nome'),
                ('data_nascimento',
                'gestante',
                'raca_cor'),
                ('municipio_residencia',
                'bairro'),
                ('logradouro',
                'numero_residencia'),
                ('municipio_ocorrencia',
                'bairro_ocorrencia'),
                ('logradouro_ocorrencia',
                'numero_ocorrencia'),
                'hora_ocorrencia',
                ('local_ocorrencia',
                'local_ocorrencia_outros'),
                'reicidencia',
                 'lesao_auto_provocada',
                ('motivo_violencia',
                'motivo_violencia_outros'),
                'tipo_violencia',
                ('meio_agressao',
                'meio_agressao_outros'),
                ('tipo_violencia_sexual',
                'tipo_violencia_sexual_outros'),
                ('procedimento_realizado',
                'numero_envolvidos'),
                ('parentesco',
                'sexo_agressor'),
                ('uso_alcool',
                'encaminhamento'),
            )
        }),
        ('Dados gerais', {
            'fields': (
                ('tipo_notificacao',
                'agravo_doenca'),
                ('codigo_cid10',
                'data_notificacao'),
                ('uf_notificacao',
                'municipio_notificacao'),
                ('codigo_ibge_notificacao',
                'unidade_notificadora'),
                ('nome_unidade_notificadora',
                'codigo_unidade'),
                ('unidade_saude',
                'codigo_cnes'),
                       )
        }),

        ('Notificação individual', {
            'fields': (
                ('idade',
                'sexo',
                'escolaridade'),
                ('numero_sus',
                'nome_mae')
            )

        }),

        ('Dados de Residência', {
            'fields': (
                ('uf_residencia',
                'codigo_ibge_residencia'),
                ('distrito',
                'codigo'),
                'complemento',
                ('geo_campo1',
                'geo_campo2'),
                ('ponto_referencia',
                'cep'),
                ('telefone',
                'zona_moradia'),
                'pais_residencia',
            )

        }),

        ('Dados da pessoa atendida', {
            'fields': (
                'nome_social',
                ('ocupacao',
                'estado_civil'),
                ('orientacao_sexual',
                'identidade_genero'),
                ('deficiencia',
                'deficiencia_se_sim'),
            )

        }),

        ('Dadis da ocorrência', {
            'fields': (
                ('uf_ocorrencia',
                'codigo_ibge_ocorrencia'),
                ('distrito_ocorrencia',
                'codigo_ocorrencia'),
                'complemento_ocorrencia',
                ('geo_campo3',
                'geo_campo4'),
                ('ponto_referencia_ocorrencia',
                'zona_ocorrencia'),
            )

        }),
        ('Dados do provável autor da violência', {
            'fields': ('idade_agressor',)

        }),
        ('Dados finais', {
            'fields': (
                'violencia_trabalho',
                'violencia_trabalho_se_sim',
                'circunstancia_lesao',
                'data_encerramento',
            )

        }),
        ('Informações complementares e observações', {
            'fields': (
                ('nome_acompanhante',
                'parentesco_acompanhante'),
                'telefone_acompanhante',
                'observacoes_adicionais',
            )

        }),
        ('Notificador', {
            'fields': (
                ('notificador_municipio_unidadesaude',
                'notificador_codigo_unidadesaude'),
                ('notificador_nome',
                'notificador_funcao'),
            )

        }),

    )
    ordering = ["-data_notificacao"]
    search_fields = ("data_ocorrencia", "nome", "tipo_violencia", "encaminhamento")
    list_filter = ("nome", "tipo_violencia", "encaminhamento")
    date_hierarchy = 'data_notificacao'


    save_on_top = True

admin.site.register(Ocorrencia, OcorrenciaAdmin)



    ## Perguntas secundarias




    ## Dados complementares





    ## Notificador
