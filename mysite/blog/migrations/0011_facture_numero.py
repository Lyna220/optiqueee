# Generated by Django 4.2.1 on 2023-07-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='numero',
            field=models.CharField(default='', max_length=10),
        ),
    ]
