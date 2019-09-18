# Generated by Django 2.2.5 on 2019-09-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='department',
            field=models.IntegerField(choices=[(1, 'Limpeza'), (2, 'Manutenção'), (3, 'Piscina'), (4, 'Jardinagem')], default=1, verbose_name='Setor'),
        ),
    ]
