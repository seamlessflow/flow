# Generated by Django 4.2.5 on 2023-09-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='react',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterModelTable(
            name='react',
            table='react',
        ),
    ]
