# Generated by Django 2.2.6 on 2019-11-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0009_auto_20191118_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]