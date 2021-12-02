# Generated by Django 3.2.9 on 2021-11-30 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('pontos_turisticos', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
            preserve_default=False,
        ),
    ]
