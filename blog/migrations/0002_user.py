# Generated by Django 4.1.1 on 2022-09-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('numero', models.BigIntegerField()),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]