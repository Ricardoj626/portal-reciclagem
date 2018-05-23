from django.db import models

# Create your models here.
from django.core.mail import EmailMessage
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.template.loader import get_template
# from localflavor import
from .choices import *
from multiselectfield import MultiSelectField

class Vitima(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome completo')
    data_nascimento = models.DateField()
    municipio_residencia = models.CharField(max_length=100, help_text='Informe seu endereço')
    bairro = models.CharField(max_length=100, help_text='Informe o bairro')
    logradouro = models.CharField(max_length=100, help_text='Informe a rua/avenida')
    telefone = models.CharField(max_length=10)
    idade = models.CharField(max_length=50, choices=CH_IDADE)
    idade_outros = models.CharField(max_length=50, verbose_name='Caso outros:', blank=True, null=True)
    raca_cor = models.CharField(max_length=100, choices=CH_RACA_COR)
    medida_protetiva = models.CharField(max_length=10, verbose_name='Possui Medida Protetiva', choices=CH_SIM_NAO)
    deficiencia = MultiSelectField(verbose_name='Deficiência', choices=CH_DEFICIENCIA, help_text='Marque todas que se aplicam')

    orientacao_sexual = models.CharField(max_length=100, choices=CH_ORIENTACAO_SEXUAL, blank=True, null=True)
    instrucao = models.CharField(max_length=100, verbose_name='Instrução', choices=CH_INSTRUCAO)
    renda_individual = models.CharField(max_length=100, choices=CH_RENDA)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.nome, self.data_nascimento)

class Agressor(models.Model):
    nome_autor = models.CharField(max_length=200, verbose_name='Nome do Autor(a)')
    rg_autor = models.CharField(max_length=15, verbose_name='RG', blank=True, null=True)
    autor_foi_preso = models.CharField(max_length=10, verbose_name='Autor Já Foi Preso', choices=CH_SIM_NAO)
    autor_doenca_psicologica = models.CharField(max_length=10,
                                                verbose_name='Autor Recebe Atendimento Psicológico/Psiquiátrico',
                                                choices=CH_SIM_NAO)
    autor_necessita_atendimento_psicologica = models.CharField(max_length=10,
                                                               verbose_name='Autor Necessita de Atendimento Psicológico/Psiquiátrico',
                                                               choices=CH_SIM_NAO)
    autor_suicidio = models.CharField(max_length=10, verbose_name='Autor Já Ameaçou ou Tentou Suicídio',
                                      choices=CH_SIM_NAO)
    autor_arma = models.CharField(max_length=100, verbose_name='O Autor Possui Arma de Fogo ou Arma Branca',
                                  choices=CH_AUTOR_ARMA)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return str(self.nome_autor)


class Ocorrencia(models.Model):
    # Perguntas primarias
    vitima = models.ForeignKey(Vitima, models.SET_NULL, blank=True, null=True)
    periodo_fato = models.CharField(max_length=100, verbose_name='Período do Fato', choices=CH_PERIODO)
    ambiente_agressao = MultiSelectField(verbose_name='Ambiente da Agressão', choices=CH_AMBIENTE, help_text='Marque todas que se aplicam')
    ambiente_agressao_outros = models.CharField(max_length=300, verbose_name='Caso outros:', blank=True, null=True)
    vinculo_agressor = models.CharField(max_length=100, verbose_name='Vínculo Do Agressor(a) Com a Vítima', choices=CH_VINCULO)
    vinculo_agressor_outros = models.CharField(max_length=100, verbose_name='Caso outros:', blank=True, null=True)
    fatores_risco = MultiSelectField(verbose_name='Fatores de Risco Identificados', choices=CH_FATORES_RISCO, help_text='Marque todas que se aplicam')
    periodo_relacionamento = models.CharField(max_length=100, verbose_name='Período De Relacionamento', choices=CH_PERIODO_RELACIONAMENTO)
    periodo_violencia = models.CharField(max_length=100, verbose_name='Há Quanto Tempo Ocorre a Violência', choices=CH_PERIODO_RELACIONAMENTO)
    filhos = models.CharField(max_length=10, verbose_name='Possui filhos', choices=CH_SIM_NAO)
    autor = models.ForeignKey(Agressor, models.SET_NULL, blank=True, null=True)


    atendimento_medico = models.CharField(max_length=10, verbose_name='Houve Atendimento Médico', choices=CH_SIM_NAO)
    tipo_violencia = MultiSelectField(verbose_name='Tipo De Violência', choices=CH_TIPO_VIOLENCIA, help_text='Marque todas que se aplicam')
    natureza_ocorrencia = MultiSelectField(verbose_name='Natureza Da Ocorrência', choices=CH_NATUREZA_OCORRENCIA, help_text='Marque todas que se aplicam')
    natureza_ocorrencia_outros = models.CharField(max_length=1000, verbose_name='Caso outros:', blank=True, null=True)
    acompanhamento_ppdv = models.CharField(max_length=10, verbose_name='Acompanhamento Pela PPVD', choices=CH_SIM_NAO)


    data_visita_autor = models.DateField(verbose_name='Data da Visita ao Autor')
    numero_reds_autor = models.CharField(max_length=20, verbose_name='Número do REDS')
    observacoes_visita_autor = models.TextField(max_length=2000, verbose_name='Observações')
    data_visita_vitima = models.DateField(verbose_name='Data da Visita A Vítima')
    numero_reds_vitima = models.CharField(max_length=20, verbose_name='Número do REDS')
    observacoes_visita_vitima = models.TextField(max_length=2000, verbose_name='Observações')

    data_visita_autor_medida_protetiva = models.DateField(verbose_name='Data da Visita ao Autor (Medida Protetiva)')
    numero_reds_autor_medida_protetiva = models.CharField(max_length=20, verbose_name='Número do REDS')
    observacoes_visita_autor_medida_protetiva = models.TextField(max_length=2000, verbose_name='Observações')
    data_visita_vitima_medida_protetiva = models.DateField(verbose_name='Data da Visita A Vítima (Medida Protetiva)')
    numero_reds_vitima_medida_protetiva = models.CharField(max_length=20, verbose_name='Número do REDS')
    observacoes_visita_vitima_medida_protetiva = models.TextField(max_length=2000, verbose_name='Observações')
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return "%s - %s" % (self.vitima, self.autor)


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

        instance.check_financeiro = True
        instance.save()
    except:
        pass
post_save.connect(post_save_relatorio_receiver, sender=Ocorrencia)