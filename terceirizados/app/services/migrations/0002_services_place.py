# Generated by Django 2.2.5 on 2019-09-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='place',
            field=models.CharField(default=1, max_length=150, verbose_name='Local'),
            preserve_default=False,
        ),
    ]