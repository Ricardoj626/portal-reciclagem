# Generated by Django 2.0.4 on 2018-04-24 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0002_auto_20180421_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ocorrencia',
            old_name='Data_notificacao',
            new_name='data_notificacao',
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='tipo_violencia_sexual_outros',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Outros'),
        ),
    ]
