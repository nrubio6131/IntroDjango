# Generated by Django 4.1.1 on 2022-09-24 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_user_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='creacion',
            new_name='datecreation',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='numero',
            new_name='number',
        ),
    ]
