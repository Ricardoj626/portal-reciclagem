# Generated by Django 2.0.4 on 2018-05-31 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('municipio', models.CharField(help_text='Informe o município da sede da empresa', max_length=100)),
                ('categoria', models.CharField(choices=[('1', 'Categoria 1'), ('2', 'Categoria 2'), ('3', 'Categoria 3'), ('4', 'Categoria 4')], max_length=100)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(help_text='Ex: 2000 para 2 toneladas do produto', verbose_name='Quantidade atual em estoque (kg)')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(help_text='Informe o endereço', max_length=100)),
                ('categoria', models.CharField(choices=[('1', 'Categoria 1'), ('2', 'Categoria 2'), ('3', 'Categoria 3'), ('4', 'Categoria 4')], max_length=100)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industria.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industria.Empresa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('necessidade', models.PositiveIntegerField(help_text='Ex: 2000 para 2 toneladas do produto', verbose_name='Necessidade média mensal (kg)')),
                ('minimo', models.PositiveIntegerField(help_text='Ex: 2000 para 2 toneladas do produto', verbose_name='Volume mínimo necessário (kg)')),
                ('maximo', models.PositiveIntegerField(help_text='Ex: 2000 para 2 toneladas do produto', verbose_name='Volume máximo suportado (kg)')),
                ('validade', models.PositiveIntegerField(help_text='Tempo dado em dias', verbose_name='Tempo de validade')),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='estoque',
            name='fabrica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industria.Fabrica'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industria.Produto'),
        ),
    ]