# Generated by Django 2.0.3 on 2018-03-31 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrega',
            old_name='complementoo',
            new_name='complemento',
        ),
    ]
