# Generated by Django 4.1.2 on 2022-10-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodotto',
            name='offerta',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]