# Generated by Django 4.2.7 on 2023-11-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('rate',), name='rating_rate_uniqueness'),
        ),
    ]
