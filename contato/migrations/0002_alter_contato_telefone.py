# Generated by Django 4.1.7 on 2023-05-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='Telefone',
            field=models.CharField(max_length=11),
        ),
    ]
