# Generated by Django 4.2.5 on 2023-09-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('team', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=200)),
            ],
        ),
    ]
