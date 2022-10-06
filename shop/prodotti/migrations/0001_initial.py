# Generated by Django 4.1.2 on 2022-10-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('prezzo', models.FloatField()),
                ('scorta', models.IntegerField()),
                ('img_url', models.CharField(max_length=2083)),
                ('fornitore', models.CharField(max_length=45)),
            ],
        ),
    ]