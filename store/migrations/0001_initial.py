# Generated by Django 2.2.7 on 2020-03-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('dia', models.CharField(max_length=200)),
                ('horario', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=200)),
                ('despedida', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'ordering': ['-created'],
            },
        ),
    ]
