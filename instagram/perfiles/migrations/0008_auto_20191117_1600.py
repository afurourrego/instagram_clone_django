# Generated by Django 2.2.6 on 2019-11-17 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0007_auto_20191116_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='sexo',
            field=models.CharField(blank=True, choices=[('m', 'Mujer'), ('h', 'Hombre'), ('n', 'No_definido')], default='m', max_length=1, null=True),
        ),
    ]
