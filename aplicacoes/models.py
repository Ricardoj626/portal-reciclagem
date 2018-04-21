from django.core.mail import EmailMessage
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.template.loader import get_template
# from localflavor import

CH_GESTANTE = [
    ('1tri','1º trimestre'),
    ('2tri','2º trimestre'),
    ('3tri','3º trimestre'),
    ('nao','Não'),
    ('na','Não se apliica')

]

CH_RACA_COR = [
    ('BRANCO','Branco'),
    ('PRETO','Preto'),
    ('AMARELO','Amarelo'),
    ('PARDO','Pardo'),
    ('INDIGENA','Indigena')
]

CH_LOCAL = [
    ('RE','Residencia'),
    ('HC','Habilitação coletiva'),
    ('ES','Escola'),
    ('LPE','Local de prática esportiva'),
    ('BA','Bar ou similar'),
    ('VP','Via pública'),
    ('CS','Comercio/Serviços'),
    ('IC','Industrias/construção'),
    ('OU','Outros')
]

CH_SIM_NAO = [
    ('S','Sim'),
    ('N','Não')
]

CH_MOTIVO = [
    ('SE','Sexismo'),
    ('HO','Homofobia'),
    ('RA','Racismo'),
    ('IR','Intolerancia religiosa'),
    ('XE','Xenofobia'),
    ('CG','Conflito geracional'),
    ('SR','Situação de rua'),
    ('DE','Deficiencia'),
    ('OU','Outros')
]

CH_TIPO_VIOLENCIA = [
    ('FI','Física'),
    ('PM','Psicológica/moral'),
    ('TO','Tortura'),
    ('SE','Sexual'),
    ('TSH','Trafico de seres humanos'),
    ('FE','Financeira/economica'),
    ('NA','Negligencia/abandono')

]

CH_UNIDADE_NOTIFICADORA = [
    ('1','Unidadede Saúde'),
    ('2','Unidade de Assistência Social'),
    ('3','Estabelecimento de Ensino'),
    ('4','Conselho Tutelar'),
    ('5','Unidade de Saúde Indígena'),
    ('6','Centro Especializado de Atendimento à Mulher'),
    ('7','Outros')
]

CH_SEXO = [
    ('M','Masculino'),
    ('F','Feminino'),
    ('I','Ignorado')
]

CH_ESCOLARIDADE = [
    ('NL','Não da para ler')
]

CH_MEIO_AGRESSAO = [
    ('FCE','Forca corporal/espancamento'),
    ('EN','Enforcamento'),
    ('OC','Objeto contundente'),
    ('OPC','Objeto pérfuro-cortante'),
    ('SOQ','Substâncias/Objeto quente'),
    ('EI','Envenenamento/Intoxicação'),
    ('AF','Arma de fogo'),
    ('AM','Ameaça'),
    ('OU','Outros')
]

CH_TIPO_VIOLENCIA_SEXUAL = [
    ('','Assédio sexual'),
    ('','Estupro'),
    ('','Pornografia infantil'),
    ('','Exploração sexual'),
    ('','Outros')
]

CH_PROCEDIMENTO = [
    ('PDST','Profilaxia DST'),
    ('PHIV','Profilaxia HIV'),
    ('PHB','Profilaxia Hepatite B'),
    ('CSA','Coleta de sangue'),
    ('CSE','Coleta de sémen'),
    ('CSV','Coleta de secreção vaginal'),
    ('CE','Contracepção de emergência'),
    ('APL','Aborto previsto em lei')
]

CH_ENVOLVIDOS = [
    ('1','Um'),
    ('2','Dois ou mais'),
    ('9','Ignorado')
]

CH_PARENTESCO = [
    ('PAI','Pai'),
    ('MAE','Mãe'),
    ('PADRASTO','Padastro'),
    ('MADRASTA','Madrasta'),
    ('CONJUGE','Cônjuge'),
    ('EXCONJUGE','Ex-Cônjuge'),
    ('NAMORADO','Namorado(a)'),
    ('EXNAMORADO','Ex-Namorado(a)'),
    ('FILHO','Filho(a)'),
    ('IRMAO','Irmão(a)'),
    ('AMIGOCONHECIDO','Amigos/Conhecidos'),
    ('DESCONHECIDO','Desconhecido(a)'),
    ('CUIDADOR','Cuidador(a)'),
    ('PATRAO','Patrão/Chefe'),
    ('PESSOAINSTITUCIONAL','Pessoa com relação institucional'),
    ('AGENTEDALEI','Policial/agente da lei'),
    ('PROPRIAPESSOA','Própria pessoa'),
    ('OUTROS','Outros')
]

CH_SEXO_AGRESSOR = [
    ('1','Masculino'),
    ('2','Feminino'),
    ('3','Ambos os sexos'),
    ('9','Ignorado')
]

CH_SIM_NAO_I = [
    ('1','Sim'),
    ('2','Não'),
    ('9', 'Ignorado' )
]

CH_SIM_NAO_NAOAPLICA_I = [
    ('1','Sim'),
    ('2','Não'),
    ('2','Não se aplica'),
    ('9', 'Ignorado' )
]

CH_ENCAMINHAMENTO = [
    ('1','Rede de Saúde (Unidade Básica de Saúde, hospitais, outras)'),
    ('2','Rede da Assistência Social (CRAS, CREAS, outras'),
    ('3','Rede de Educação (Creche, escolas, outras'),
    ('4','Rede de atendimento à Mulher (Centro Especializado de Atendimento à Mulher, Casa da Mulher Brasileira, outras)'),
    ('5','Conselho Tutelas'),
    ('6','Conselho do Idoso'),
    ('7','Delegacia de Atendimento ao  Idoso'),
    ('8','Centro de Referência dos Direitos Humanos'),
    ('9','Ministério Público'),
    ('10','Delegacia Especializada de Proteção à Criança e Adolescente'),
    ('11','Delegacia de Atendimento à Mulher'),
    ('12','Outras delegacias'),
    ('13','Justiça da infância e da Juventude'),
    ('14','Defensoria Pública')
]

CH_ZONA = [
    ('1','Urbana'),
    ('2','Rural'),
    ('3','Periurbana'),
    ('9','Ignorado'),
]

CH_ESTADO_CIVIL = [
    ('1','Solteiro'),
    ('2','Casado/união consensual'),
    ('3','Viúvo'),
    ('4',' Separado'),
    ('8','Não se aplica'),
    ('9','Ignorado')
]

CH_ORIENTACAO_SEXUAL = [
    ('1','Heterossexual'),
    ('2','Homossexual (gay/lesbuca)'),
    ('3','Bissexual'),
    ('8','Não se aplica'),
    ('9','Ignorado')
]

CH_IDENTIDADE_GENERO = [
    ('1','Travesti'),
    ('2','Mulher Transexual'),
    ('3','Homem Transexual'),
    ('8','Não se aplica'),
    ('9','Ignorado')
]

CH_DEFICIENCIA = [
    ('1','Deficiência Física'),
    ('2','Deficiência Intelectual'),
    ('3','Deficiência Visual'),
    ('4','Deficiência auditiva'),
    ('5','Transtorno mental'),
    ('6','Transtorno  de comportamento'),
    ('9','Outras')
]

CH_ZONA_OCORRENCIA = [
    ('','Urbana'),
    ('','Rural'),
    ('','Periurbana'),
    ('','Ignorado')
]

CH_IDADE_AGRESSOR = [
    ('1','Criança (0 a 9 anos)'),
    ('2','Adolecente (10 a 19 anos)'),
    ('3','Jovem (20 a 24 anos)'),
    ('4','Pessoa adulta (25 a 59 anos'),
    ('5','Pessoa idosa ( 60 anos ou mais'),
    ('9','Ignorado'),
]

class Ocorrencia(models.Model):
    ## Perguntas primarias
    data_ocorrencia = models.DateTimeField() # 9
    nome = models.CharField(max_length=100, help_text='Informe o nome do paciente') # 10
    data_nascimento = models.DateField(auto_now_add=False) # 11
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
    hora_ocorrencia = models.CharField(max_length=5, help_text='(00:00 - 23:59') # 51
    local_ocorrencia = models.CharField(max_length=100, choices=CH_LOCAL) # 52
    local_ocorrencia_outros = models.CharField(max_length=200, verbose_name='Outros', blank=True, null=True) # 52 complemento
    reicidencia = models.CharField(max_length=100, verbose_name='Ocorreu outras vezes?', choices=CH_SIM_NAO) # 53
    lesao_auto_provocada = models.CharField(max_length=100, verbose_name='A lesão foi auto provocada', choices=CH_SIM_NAO) # 54
    motivo_violencia = models.CharField(max_length=200, verbose_name='Essa violencia foi motivada por', choices=CH_MOTIVO) # 55
    motivo_violencia_outros = models.CharField(max_length=200, verbose_name='Outros', blank=True, null=True) # 55 complemento
    tipo_violencia = models.CharField(max_length=100, help_text='Informe o tipo de violência', choices=CH_TIPO_VIOLENCIA) # 56
    meio_agressao = models.CharField(max_length=200, verbose_name='Meio de agressão', choices=CH_MEIO_AGRESSAO) # 57
    meio_agressao_outros =  models.CharField(max_length=200, verbose_name='Outros' , blank=True, null=True) # 57 complemento
    tipo_violencia_sexual = models.CharField(max_length=200, choices=CH_TIPO_VIOLENCIA_SEXUAL, verbose_name='Se ocorreu violência secual, qual o tipo?') # 58
    tipo_violencia_sexual_outros = models.CharField(max_length=200, verbose_name='Outros') # 58 complemento
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
    Data_notificacao = models.DateField(auto_now_add=True, blank=True, null=True)
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
    uf_residencia = models.CharField(max_length=2, verbose_name='UF (residência)')
    codigo_ibge_residencia = models.CharField(max_length=6, verbose_name='Código (IBGE) (Residência)')
    distrito = models.CharField(max_length=200)
    codigo = models.CharField(max_length=6, verbose_name='Código')
    complemento = models.CharField(max_length=200, verbose_name='Complemento (apto, casa, ...')
    geo_campo1 = models.CharField(max_length=100, verbose_name='Geo campo 1')
    geo_campo2 = models.CharField(max_length=100, verbose_name='Geo campo 2')
    ponto_referencia = models.CharField(max_length=200, verbose_name='Ponto de Referência')
    cep = models.CharField(max_length=7, verbose_name='CEP')
    telefone = models.CharField(max_length=10)
    zona_moradia = models.CharField(max_length=20, verbose_name='Zona', choices=CH_ZONA)
    pais_residencia = models.CharField(max_length=100, verbose_name='País (se residente fora do Brasil')

    ## Dados complementares
    nome_social = models.CharField(max_length=100)
    ocupacao = models.CharField(max_length=100, verbose_name='Ocupação')
    estado_civil = models.CharField(max_length=100, verbose_name='Situação conjugal/Estado civil', choices=CH_ESTADO_CIVIL)
    orientacao_sexual = models.CharField(max_length=100, choices=CH_ORIENTACAO_SEXUAL)
    identidade_genero = models.CharField(max_length=100, verbose_name='Identidade de gênero', choices=CH_IDENTIDADE_GENERO)
    deficiencia = models.CharField(max_length=100, verbose_name='Possui algum tipo de deficiência/transtorno?', choices=CH_SIM_NAO_I)
    deficiencia_se_sim = models.CharField(max_length=200, verbose_name='Se sim, qual tipo de deficiência/transtorno?', choices=CH_DEFICIENCIA)
    uf_ocorrencia = models.CharField(max_length=2)
    codigo_ibge_ocorrencia = models.CharField(max_length=6, verbose_name='Código (IBGE) (Ocorrência)')
    distrito_ocorrencia = models.CharField(max_length=100)
    codigo_ocorrencia = models.CharField(max_length=6,  verbose_name='Código')
    complemento_ocorrencia = models.CharField(max_length=100, verbose_name='Complemento (apto, casa, ...)')
    geo_campo3 = models.CharField(max_length=100, verbose_name='Geo campo 3')
    geo_campo4 = models.CharField(max_length=100, verbose_name='Geo campo 4')
    ponto_referencia_ocorrencia = models.CharField(max_length=200, verbose_name='Ponto de referência')
    zona_ocorrencia = models.CharField(max_length=100, verbose_name='Zona', choices=CH_ZONA_OCORRENCIA)
    idade_agressor = models.CharField(max_length=100, verbose_name=CH_IDADE_AGRESSOR)
    violencia_trabalho = models.CharField(max_length=20, verbose_name='Violência Relacionada ao Trabalho', choices=CH_SIM_NAO_I)
    violencia_trabalho_se_sim = models.CharField(max_length=20, verbose_name='Se sim, foi emitida a Comunicaçao de Acidente de Trabalho (CAT)', choices=CH_SIM_NAO_NAOAPLICA_I)
    circunstancia_lesao = models.CharField(max_length=5, verbose_name='Circunstâncias da lesão', help_text='CID 10 - Cap XX')
    data_encerramento = models.DateField()

    ## Informações complementares e observações
    nome_acompanhante = models.CharField(max_length=200, verbose_name='Nome do acompanhante')
    parentesco_acompanhante = models.CharField(max_length=100, verbose_name='Vinculo/grau de parentesco')
    telefone_acompanhante = models.CharField(max_length=10, verbose_name='(DDD) Telefone')
    observacoes_adicionais = models.TextField(max_length=4000, verbose_name='Observações Adicionais')

    ## Notificador
    notificador_municipio_unidadesaude = models.CharField(max_length=200, verbose_name='Município/Unidade de Saúde')
    notificador_codigo_unidadesaude = models.CharField(max_length=8, verbose_name='Cod. da Unid. de Saúde/CNES')
    notificador_nome = models.CharField(max_length=200)
    notificador_funcao = models.CharField(max_length=200)




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