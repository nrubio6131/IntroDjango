# Generated by Django 4.1.1 on 2022-09-24 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_user_email_user_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='file',
        ),
    ]
