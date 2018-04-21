# Generated by Django 2.0.4 on 2018-04-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ocorrencia', models.DateTimeField()),
                ('nome', models.CharField(help_text='Informe o nome do paciente', max_length=100)),
                ('data_nascimento', models.DateField()),
                ('gestante', models.CharField(choices=[('1tri', '1º trimestre'), ('2tri', '2º trimestre'), ('3tri', '3º trimestre'), ('nao', 'Não'), ('na', 'Não se apliica')], max_length=100)),
                ('raca_cor', models.CharField(choices=[('BRANCO', 'Branco'), ('PRETO', 'Preto'), ('AMARELO', 'Amarelo'), ('PARDO', 'Pardo'), ('INDIGENA', 'Indigena')], max_length=100)),
                ('municipio_residencia', models.CharField(help_text='Informe seu endereço', max_length=100)),
                ('bairro', models.CharField(help_text='Informe o bairro', max_length=100)),
                ('logradouro', models.CharField(help_text='Informe a rua/avenida', max_length=100)),
                ('numero_residencia', models.PositiveIntegerField(verbose_name='Número')),
                ('municipio_ocorrencia', models.CharField(help_text='Informe onde houve a ocorrencia', max_length=100, verbose_name='Município da ocorrência')),
                ('bairro_ocorrencia', models.CharField(help_text='Informe o bairro', max_length=100)),
                ('logradouro_ocorrencia', models.CharField(help_text='Informe a rua/avenida', max_length=100)),
                ('numero_ocorrencia', models.PositiveIntegerField(verbose_name='Número')),
                ('hora_ocorrencia', models.CharField(help_text='(00:00 - 23:59', max_length=5)),
                ('local_ocorrencia', models.CharField(choices=[('RE', 'Residencia'), ('HC', 'Habilitação coletiva'), ('ES', 'Escola'), ('LPE', 'Local de prática esportiva'), ('BA', 'Bar ou similar'), ('VP', 'Via pública'), ('CS', 'Comercio/Serviços'), ('IC', 'Industrias/construção'), ('OU', 'Outros')], max_length=100)),
                ('local_ocorrencia_outros', models.CharField(blank=True, max_length=200, null=True, verbose_name='Outros')),
                ('reicidencia', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=100, verbose_name='Ocorreu outras vezes?')),
                ('lesao_auto_provocada', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=100, verbose_name='A lesão foi auto provocada')),
                ('motivo_violencia', models.CharField(choices=[('SE', 'Sexismo'), ('HO', 'Homofobia'), ('RA', 'Racismo'), ('IR', 'Intolerancia religiosa'), ('XE', 'Xenofobia'), ('CG', 'Conflito geracional'), ('SR', 'Situação de rua'), ('DE', 'Deficiencia'), ('OU', 'Outros')], max_length=200, verbose_name='Essa violencia foi motivada por')),
                ('motivo_violencia_outros', models.CharField(blank=True, max_length=200, null=True, verbose_name='Outros')),
                ('tipo_violencia', models.CharField(choices=[('FI', 'Física'), ('PM', 'Psicológica/moral'), ('TO', 'Tortura'), ('SE', 'Sexual'), ('TSH', 'Trafico de seres humanos'), ('FE', 'Financeira/economica'), ('NA', 'Negligencia/abandono')], help_text='Informe o tipo de violência', max_length=100)),
                ('meio_agressao', models.CharField(choices=[('FCE', 'Forca corporal/espancamento'), ('EN', 'Enforcamento'), ('OC', 'Objeto contundente'), ('OPC', 'Objeto pérfuro-cortante'), ('SOQ', 'Substâncias/Objeto quente'), ('EI', 'Envenenamento/Intoxicação'), ('AF', 'Arma de fogo'), ('AM', 'Ameaça'), ('OU', 'Outros')], max_length=200, verbose_name='Meio de agressão')),
                ('meio_agressao_outros', models.CharField(blank=True, max_length=200, null=True, verbose_name='Outros')),
                ('tipo_violencia_sexual', models.CharField(choices=[('', 'Assédio sexual'), ('', 'Estupro'), ('', 'Pornografia infantil'), ('', 'Exploração sexual'), ('', 'Outros')], max_length=200, verbose_name='Se ocorreu violência secual, qual o tipo?')),
                ('tipo_violencia_sexual_outros', models.CharField(max_length=200, verbose_name='Outros')),
                ('procedimento_realizado', models.CharField(choices=[('PDST', 'Profilaxia DST'), ('PHIV', 'Profilaxia HIV'), ('PHB', 'Profilaxia Hepatite B'), ('CSA', 'Coleta de sangue'), ('CSE', 'Coleta de sémen'), ('CSV', 'Coleta de secreção vaginal'), ('CE', 'Contracepção de emergência'), ('APL', 'Aborto previsto em lei')], max_length=100)),
                ('numero_envolvidos', models.CharField(choices=[('1', 'Um'), ('2', 'Dois ou mais'), ('9', 'Ignorado')], max_length=40, verbose_name='Número de envolvidos')),
                ('parentesco', models.CharField(choices=[('PAI', 'Pai'), ('MAE', 'Mãe'), ('PADRASTO', 'Padastro'), ('MADRASTA', 'Madrasta'), ('CONJUGE', 'Cônjuge'), ('EXCONJUGE', 'Ex-Cônjuge'), ('NAMORADO', 'Namorado(a)'), ('EXNAMORADO', 'Ex-Namorado(a)'), ('FILHO', 'Filho(a)'), ('IRMAO', 'Irmão(a)'), ('AMIGOCONHECIDO', 'Amigos/Conhecidos'), ('DESCONHECIDO', 'Desconhecido(a)'), ('CUIDADOR', 'Cuidador(a)'), ('PATRAO', 'Patrão/Chefe'), ('PESSOAINSTITUCIONAL', 'Pessoa com relação institucional'), ('AGENTEDALEI', 'Policial/agente da lei'), ('PROPRIAPESSOA', 'Própria pessoa'), ('OUTROS', 'Outros')], max_length=200, verbose_name='Veículo/grau de parentesco com a pessoa atendida')),
                ('sexo_agressor', models.CharField(choices=[('1', 'Masculino'), ('2', 'Feminino'), ('3', 'Ambos os sexos'), ('9', 'Ignorado')], max_length=100)),
                ('uso_alcool', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=10, verbose_name='Suspeita de uso de álcool')),
                ('encaminhamento', models.CharField(choices=[('1', 'Rede de Saúde (Unidade Básica de Saúde, hospitais, outras)'), ('2', 'Rede da Assistência Social (CRAS, CREAS, outras'), ('3', 'Rede de Educação (Creche, escolas, outras'), ('4', 'Rede de atendimento à Mulher (Centro Especializado de Atendimento à Mulher, Casa da Mulher Brasileira, outras)'), ('5', 'Conselho Tutelas'), ('6', 'Conselho do Idoso'), ('7', 'Delegacia de Atendimento ao  Idoso'), ('8', 'Centro de Referência dos Direitos Humanos'), ('9', 'Ministério Público'), ('10', 'Delegacia Especializada de Proteção à Criança e Adolescente'), ('11', 'Delegacia de Atendimento à Mulher'), ('12', 'Outras delegacias'), ('13', 'Justiça da infância e da Juventude'), ('14', 'Defensoria Pública')], max_length=300)),
                ('tipo_notificacao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipo de notificação')),
                ('agravo_doenca', models.CharField(blank=True, max_length=100, null=True, verbose_name='Agravo/doença')),
                ('codigo_cid10', models.CharField(blank=True, max_length=100, null=True, verbose_name='Código (CID10')),
                ('Data_notificacao', models.DateField(auto_now_add=True, null=True)),
                ('uf_notificacao', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF (Notificação)')),
                ('municipio_notificacao', models.CharField(blank=True, max_length=200, null=True)),
                ('codigo_ibge_notificacao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Código (IBGE) (Notificacao)')),
                ('unidade_notificadora', models.CharField(blank=True, choices=[('1', 'Unidadede Saúde'), ('2', 'Unidade de Assistência Social'), ('3', 'Estabelecimento de Ensino'), ('4', 'Conselho Tutelar'), ('5', 'Unidade de Saúde Indígena'), ('6', 'Centro Especializado de Atendimento à Mulher'), ('7', 'Outros')], max_length=100, null=True)),
                ('nome_unidade_notificadora', models.CharField(blank=True, max_length=256, null=True, verbose_name='Nome da Unidade Notificadora')),
                ('codigo_unidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Código Unidade')),
                ('unidade_saude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Unidade de Saúde')),
                ('codigo_cnes', models.CharField(blank=True, max_length=7, null=True, verbose_name='Código (CNES)')),
                ('idade', models.CharField(blank=True, max_length=20, null=True, verbose_name='(ou) Idade')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('I', 'Ignorado')], max_length=50, null=True)),
                ('escolaridade', models.CharField(blank=True, choices=[('NL', 'Não da para ler')], max_length=300, null=True)),
                ('numero_sus', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número do Cartão SUS')),
                ('nome_mae', models.CharField(blank=True, max_length=256, null=True, verbose_name='Nome da mãe')),
                ('uf_residencia', models.CharField(max_length=2, verbose_name='UF (residência)')),
                ('codigo_ibge_residencia', models.CharField(max_length=6, verbose_name='Código (IBGE) (Residência)')),
                ('distrito', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=6, verbose_name='Código')),
                ('complemento', models.CharField(max_length=200, verbose_name='Complemento (apto, casa, ...')),
                ('geo_campo1', models.CharField(max_length=100, verbose_name='Geo campo 1')),
                ('geo_campo2', models.CharField(max_length=100, verbose_name='Geo campo 2')),
                ('ponto_referencia', models.CharField(max_length=200, verbose_name='Ponto de Referência')),
                ('cep', models.CharField(max_length=7, verbose_name='CEP')),
                ('telefone', models.CharField(max_length=10)),
                ('zona_moradia', models.CharField(choices=[('1', 'Urbana'), ('2', 'Rural'), ('3', 'Periurbana'), ('9', 'Ignorado')], max_length=20, verbose_name='Zona')),
                ('pais_residencia', models.CharField(max_length=100, verbose_name='País (se residente fora do Brasil')),
                ('nome_social', models.CharField(max_length=100)),
                ('ocupacao', models.CharField(max_length=100, verbose_name='Ocupação')),
                ('estado_civil', models.CharField(choices=[('1', 'Solteiro'), ('2', 'Casado/união consensual'), ('3', 'Viúvo'), ('4', ' Separado'), ('8', 'Não se aplica'), ('9', 'Ignorado')], max_length=100, verbose_name='Situação conjugal/Estado civil')),
                ('orientacao_sexual', models.CharField(choices=[('1', 'Heterossexual'), ('2', 'Homossexual (gay/lesbuca)'), ('3', 'Bissexual'), ('8', 'Não se aplica'), ('9', 'Ignorado')], max_length=100)),
                ('identidade_genero', models.CharField(choices=[('1', 'Travesti'), ('2', 'Mulher Transexual'), ('3', 'Homem Transexual'), ('8', 'Não se aplica'), ('9', 'Ignorado')], max_length=100, verbose_name='Identidade de gênero')),
                ('deficiencia', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=100, verbose_name='Possui algum tipo de deficiência/transtorno?')),
                ('deficiencia_se_sim', models.CharField(choices=[('1', 'Deficiência Física'), ('2', 'Deficiência Intelectual'), ('3', 'Deficiência Visual'), ('4', 'Deficiência auditiva'), ('5', 'Transtorno mental'), ('6', 'Transtorno  de comportamento'), ('9', 'Outras')], max_length=200, verbose_name='Se sim, qual tipo de deficiência/transtorno?')),
                ('uf_ocorrencia', models.CharField(max_length=2)),
                ('codigo_ibge_ocorrencia', models.CharField(max_length=6, verbose_name='Código (IBGE) (Ocorrência)')),
                ('distrito_ocorrencia', models.CharField(max_length=100)),
                ('codigo_ocorrencia', models.CharField(max_length=6, verbose_name='Código')),
                ('complemento_ocorrencia', models.CharField(max_length=100, verbose_name='Complemento (apto, casa, ...)')),
                ('geo_campo3', models.CharField(max_length=100, verbose_name='Geo campo 3')),
                ('geo_campo4', models.CharField(max_length=100, verbose_name='Geo campo 4')),
                ('ponto_referencia_ocorrencia', models.CharField(max_length=200, verbose_name='Ponto de referência')),
                ('zona_ocorrencia', models.CharField(choices=[('', 'Urbana'), ('', 'Rural'), ('', 'Periurbana'), ('', 'Ignorado')], max_length=100, verbose_name='Zona')),
                ('idade_agressor', models.CharField(max_length=100, verbose_name=[('1', 'Criança (0 a 9 anos)'), ('2', 'Adolecente (10 a 19 anos)'), ('3', 'Jovem (20 a 24 anos)'), ('4', 'Pessoa adulta (25 a 59 anos'), ('5', 'Pessoa idosa ( 60 anos ou mais'), ('9', 'Ignorado')])),
                ('violencia_trabalho', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('9', 'Ignorado')], max_length=20, verbose_name='Violência Relacionada ao Trabalho')),
                ('violencia_trabalho_se_sim', models.CharField(choices=[('1', 'Sim'), ('2', 'Não'), ('2', 'Não se aplica'), ('9', 'Ignorado')], max_length=20, verbose_name='Se sim, foi emitida a Comunicaçao de Acidente de Trabalho (CAT)')),
                ('circunstancia_lesao', models.CharField(help_text='CID 10 - Cap XX', max_length=5, verbose_name='Circunstâncias da lesão')),
                ('data_encerramento', models.DateField()),
                ('nome_acompanhante', models.CharField(max_length=200, verbose_name='Nome do acompanhante')),
                ('parentesco_acompanhante', models.CharField(max_length=100, verbose_name='Vinculo/grau de parentesco')),
                ('telefone_acompanhante', models.CharField(max_length=10, verbose_name='(DDD) Telefone')),
                ('observacoes_adicionais', models.TextField(max_length=4000, verbose_name='Observações Adicionais')),
                ('notificador_municipio_unidadesaude', models.CharField(max_length=200, verbose_name='Município/Unidade de Saúde')),
                ('notificador_codigo_unidadesaude', models.CharField(max_length=8, verbose_name='Cod. da Unid. de Saúde/CNES')),
                ('notificador_nome', models.CharField(max_length=200)),
                ('notificador_funcao', models.CharField(max_length=200)),
            ],
        ),
    ]
