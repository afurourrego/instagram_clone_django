# Generated by Django 2.2.6 on 2019-11-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('foto', models.ImageField(upload_to='perfiles/fotos')),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biografia', models.TextField(blank=True, max_length=1000, null=True)),
                ('sitio_web', models.CharField(blank=True, max_length=45, null=True)),
                ('sexo', models.PositiveIntegerField(blank=True, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfiles/fotos')),
            ],
        ),
    ]