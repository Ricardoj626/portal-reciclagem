# Generated by Django 2.0.4 on 2018-05-07 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0005_auto_20180507_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ocorrencia',
            old_name='dataocorrencia',
            new_name='data_ocorrencia',
        ),
    ]
