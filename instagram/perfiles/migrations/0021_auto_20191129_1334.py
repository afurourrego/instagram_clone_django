# Generated by Django 2.2.6 on 2019-11-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0020_auto_20191129_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='seguidores',
            field=models.ManyToManyField(through='perfiles.Seguidor', to='perfiles.Perfil'),
        ),
        migrations.DeleteModel(
            name='Seguidores',
        ),
    ]