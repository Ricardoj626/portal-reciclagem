from django.db import models

# Create your models here.
from django.core.mail import EmailMessage
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.template.loader import get_template
# from localflavor import
from .choices import *

class Ocorrencia(models.Model):
    ## Perguntas primarias
    data_ocorrencia = models.DateTimeField() # 9
    nome = models.CharField(max_length=100, help_text='Informe o nome do paciente') # 10
    data_nascimento = models.DateField() # 11
    gestante = models.CharField(max_length=100, choices=CH_GESTANTE)  # 14
    raca_cor = models.CharField(max_length=100, choices=CH_RACA_COR) # 15
    municipio_residencia = models.CharField(max_length=100, help_text='Informe seu endereço') # 20
    bairro = models.CharField(max_length=100, help_text='Informe o bairro') # 22
    logradouro = models.CharField(max_length=100, help_text='Informe a rua/avenida') # 23
    numero_residencia = models.PositiveIntegerField(verbose_name='Número')  # 24
    municipio_ocorrencia = models.CharField(max_length=100, help_text='Informe onde houve a ocorrencia', verbose_name='Município da ocorrência') # 40
    bairro_ocorrencia = models.CharField(max_length=100, help_text='Informe o bairro') # 43
    logradouro_ocorrencia = models.CharField(max_length=100, help_text='Informe a rua/avenida') # 44
    numero_ocorrencia = models.PositiveIntegerField(verbose_name='Número') # 45
    hora_ocorrencia = models.CharField(max_length=5, help_text='(00:00 - 23:59)') # 51
    local_ocorrencia = models.CharField(max_length=100, choices=CH_LOCAL) # 52
    local_ocorrencia_outros = models.CharField(max_length=200, verbose_name='Outros', blank=True, null=True) # 52 complemento
    reicidencia = models.CharField(max_length=100, verbose_name='Ocorreu outras vezes?', choices=CH_SIM_NAO) # 53
    lesao_auto_provocada = models.CharField(max_length=100, verbose_name='A lesão foi auto provocada', choices=CH_SIM_NAO) # 54
    motivo_violencia = models.CharField(max_length=200, verbose_name='Essa violencia foi motivada por', choices=CH_MOTIVO) # 55
    motivo_violencia_outros = models.CharField(max_length=200, verbose_name='Outros', blank=True, null=True) # 55 complemento
    tipo_violencia = models.CharField(max_length=100, help_text='Informe o tipo de violência', choices=CH_TIPO_VIOLENCIA) # 56
    meio_agressao = models.CharField(max_length=200, verbose_name='Meio de agressão', choices=CH_MEIO_AGRESSAO) # 57
    meio_agressao_outros =  models.CharField(max_length=200, verbose_name='Outros', blank=True, null=True) # 57 complemento
    tipo_violencia_sexual = models.CharField(max_length=200, choices=CH_TIPO_VIOLENCIA_SEXUAL, verbose_name='Se ocorreu violência sexual, qual o tipo?') # 58
    tipo_violencia_sexual_outros = models.CharField(max_length=200, verbose_name='Outros', blank=True, null=True) # 58 complemento
    procedimento_realizado = models.CharField(max_length=100, choices=CH_PROCEDIMENTO) # 59
    numero_envolvidos = models.CharField(max_length=40, verbose_name='Número de envolvidos', choices=CH_ENVOLVIDOS) # 60
    parentesco = models.CharField(max_length=200, choices=CH_PARENTESCO, verbose_name='Veículo/grau de parentesco com a pessoa atendida') # 61
    sexo_agressor = models.CharField(max_length=100, choices=CH_SEXO_AGRESSOR) # 62
    uso_alcool = models.CharField(max_length=10, choices=CH_SIM_NAO_I, verbose_name='Suspeita de uso de álcool') # 63
    encaminhamento = models.CharField(max_length=300, choices=CH_ENCAMINHAMENTO) # 65

    ## Perguntas secundarias
    tipo_notificacao = models.CharField(max_length=100, verbose_name='Tipo de notificação', blank=True, null=True)
    agravo_doenca =  models.CharField(max_length=100, verbose_name='Agravo/doença', blank=True, null=True)
    codigo_cid10 = models.CharField(max_length=100, verbose_name='Código (CID10', blank=True, null=True)
    data_notificacao = models.DateField(blank=True, null=True)
    uf_notificacao = models.CharField(verbose_name='UF (Notificação)', max_length=2, blank=True, null=True)
    municipio_notificacao = models.CharField(max_length=200, blank=True, null=True)
    codigo_ibge_notificacao = models.CharField(max_length=100, verbose_name='Código (IBGE) (Notificacao)', blank=True, null=True)
    unidade_notificadora = models.CharField(max_length=100, choices=CH_UNIDADE_NOTIFICADORA, blank=True, null=True)
    nome_unidade_notificadora = models.CharField(max_length=256, verbose_name='Nome da Unidade Notificadora', blank=True, null=True)
    codigo_unidade = models.CharField(max_length=100, verbose_name='Código Unidade', blank=True, null=True)
    unidade_saude = models.CharField(max_length=100,verbose_name='Unidade de Saúde', blank=True, null=True)
    codigo_cnes = models.CharField(max_length=7, verbose_name='Código (CNES)', blank=True, null=True)
    idade = models.CharField(max_length=20, verbose_name='(ou) Idade', blank=True, null=True)
    sexo = models.CharField(max_length=50, choices=CH_SEXO, blank=True, null=True)
    escolaridade = models.CharField(max_length=300, choices=CH_ESCOLARIDADE, blank=True, null=True)
    numero_sus = models.CharField(max_length=15, verbose_name='Número do Cartão SUS', blank=True, null=True)
    nome_mae = models.CharField(max_length=256, verbose_name='Nome da mãe', blank=True, null=True)
    uf_residencia = models.CharField(max_length=2, verbose_name='UF (residência)', blank=True, null=True)
    codigo_ibge_residencia = models.CharField(max_length=6, verbose_name='Código (IBGE) (Residência)', blank=True, null=True)
    distrito = models.CharField(max_length=200, blank=True, null=True)
    codigo = models.CharField(max_length=6, verbose_name='Código', blank=True, null=True)
    complemento = models.CharField(max_length=200, verbose_name='Complemento(apto, casa) ', blank=True, null=True)
    geo_campo1 = models.CharField(max_length=100, verbose_name='Geo campo 1', blank=True, null=True)
    geo_campo2 = models.CharField(max_length=100, verbose_name='Geo campo 2', blank=True, null=True)
    ponto_referencia = models.CharField(max_length=200, verbose_name='Ponto de Referência', blank=True, null=True)
    cep = models.CharField(max_length=7, verbose_name='CEP', blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    zona_moradia = models.CharField(max_length=20, verbose_name='Zona', choices=CH_ZONA, blank=True, null=True)
    pais_residencia = models.CharField(max_length=100, verbose_name='País (se residente fora do Brasil)', blank=True, null=True)

    ## Dados complementares
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    ocupacao = models.CharField(max_length=100, verbose_name='Ocupação', blank=True, null=True)
    estado_civil = models.CharField(max_length=100, verbose_name='Situação conjugal/Estado civil', choices=CH_ESTADO_CIVIL, blank=True, null=True)
    orientacao_sexual = models.CharField(max_length=100, choices=CH_ORIENTACAO_SEXUAL, blank=True, null=True)
    identidade_genero = models.CharField(max_length=100, verbose_name='Identidade de gênero', choices=CH_IDENTIDADE_GENERO, blank=True, null=True)
    deficiencia = models.CharField(max_length=100, verbose_name='Possui algum tipo de deficiência/transtorno?', choices=CH_SIM_NAO_I, blank=True, null=True)
    deficiencia_se_sim = models.CharField(max_length=200, verbose_name='Se sim, qual tipo de deficiência/transtorno?', choices=CH_DEFICIENCIA, blank=True, null=True)
    uf_ocorrencia = models.CharField(max_length=2, blank=True, null=True)
    codigo_ibge_ocorrencia = models.CharField(max_length=6, verbose_name='Código (IBGE) (Ocorrência)', blank=True, null=True)
    distrito_ocorrencia = models.CharField(max_length=100, blank=True, null=True)
    codigo_ocorrencia = models.CharField(max_length=6,  verbose_name='Código', blank=True, null=True)
    complemento_ocorrencia = models.CharField(max_length=100, verbose_name='Complemento(apto, casa)', blank=True, null=True)
    geo_campo3 = models.CharField(max_length=100, verbose_name='Geo campo 3', blank=True, null=True)
    geo_campo4 = models.CharField(max_length=100, verbose_name='Geo campo 4', blank=True, null=True)
    ponto_referencia_ocorrencia = models.CharField(max_length=200, verbose_name='Ponto de referência', blank=True, null=True)
    zona_ocorrencia = models.CharField(max_length=100, verbose_name='Zona', choices=CH_ZONA_OCORRENCIA, blank=True, null=True)
    idade_agressor = models.CharField(max_length=100,verbose_name='Ciclo de vida do provável autor da violência', choices=CH_IDADE_AGRESSOR, blank=True, null=True)
    violencia_trabalho = models.CharField(max_length=20, verbose_name='Violência Relacionada ao Trabalho', choices=CH_SIM_NAO_I, blank=True, null=True)
    violencia_trabalho_se_sim = models.CharField(max_length=20, verbose_name='Se sim, foi emitida a Comunicaçao de Acidente de Trabalho (CAT)', choices=CH_SIM_NAO_NAOAPLICA_I, blank=True, null=True)
    circunstancia_lesao = models.CharField(max_length=5, verbose_name='Circunstâncias da lesão', help_text='CID 10 - Cap XX', blank=True, null=True)
    data_encerramento = models.DateField(blank=True, null=True)

    ## Informações complementares e observações
    nome_acompanhante = models.CharField(max_length=200, verbose_name='Nome do acompanhante', blank=True, null=True)
    parentesco_acompanhante = models.CharField(max_length=100, verbose_name='Vinculo/grau de parentesco', blank=True, null=True)
    telefone_acompanhante = models.CharField(max_length=10, verbose_name='(DDD) Telefone', blank=True, null=True)
    observacoes_adicionais = models.TextField(max_length=4000, verbose_name='Observações Adicionais', blank=True, null=True)

    ## Notificador
    notificador_municipio_unidadesaude = models.CharField(max_length=200, verbose_name='Município/Unidade de Saúde', blank=True, null=True)
    notificador_codigo_unidadesaude = models.CharField(max_length=8, verbose_name='Cod. da Unid. de Saúde/CNES', blank=True, null=True)
    notificador_nome = models.CharField(max_length=200, blank=True, null=True)
    notificador_funcao = models.CharField(max_length=200, blank=True, null=True)




    def __str__(self):
        return "%s - %s" % (self.nome, self.data_ocorrencia)


def post_save_relatorio_receiver(sender, instance, *args, **kwargs):
    destinatario = "ricardoj@gec.inatel.br"
    remetente = "ricardoj@gec.inatel.br"

    try:
        subject = 'Novo Servico para Faturamento - %s : %s - %s %s (%s)' % (
            instance.tipo.servico, instance.id_behive, instance.link, instance.data_envio_pacote,
            instance.cliente.username)
        msg = get_template('outros/email_template.html').render({'relatorio': instance})
        email = EmailMessage(subject, msg, to=[destinatario, ], from_email=remetente)
        email.content_subtype = 'html'
        email.send()

        # from financeiro.models import Financeiro
        # f = Financeiro.objects.create(relatorio=instance, )
        # print(f)

        instance.check_financeiro = True
        instance.save()
    except:
        pass
post_save.connect(post_save_relatorio_receiver, sender=Ocorrencia)