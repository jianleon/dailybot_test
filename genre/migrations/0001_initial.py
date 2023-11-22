# Generated by Django 4.2.7 on 2023-11-22 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre del género')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
                'db_table': 'genre',
                'indexes': [models.Index(fields=['name'], name='genre_name_idx')],
            },
        ),
    ]
