# Generated by Django 2.2.6 on 2019-11-28 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0012_auto_20191118_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='is_historia',
            field=models.BooleanField(default=False),
        ),
    ]