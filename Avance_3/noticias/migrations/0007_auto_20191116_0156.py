# Generated by Django 2.2.6 on 2019-11-16 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_auto_20191116_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='created',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='foto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Foto'),
        ),
    ]
