# Generated by Django 2.2.6 on 2019-11-16 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0006_foto_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='user_id',
            new_name='perfil_id',
        ),
        migrations.RenameField(
            model_name='foto',
            old_name='user_id',
            new_name='perfil_id',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='perfil_id',
        ),
        migrations.RenameField(
            model_name='seguidor',
            old_name='user_id',
            new_name='perfil_id',
        ),
    ]