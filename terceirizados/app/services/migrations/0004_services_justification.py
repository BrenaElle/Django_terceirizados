# Generated by Django 2.2.5 on 2019-09-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_services_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='justification',
            field=models.TextField(default=1, verbose_name='Justificativa'),
            preserve_default=False,
        ),
    ]
