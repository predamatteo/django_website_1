# Generated by Django 4.1.2 on 2022-10-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0002_prodotto_offerta'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodotto',
            name='prezzo_in_offerta',
            field=models.FloatField(default=False),
            preserve_default=False,
        ),
    ]
