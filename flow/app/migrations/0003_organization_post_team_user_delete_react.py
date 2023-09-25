# Generated by Django 4.2.5 on 2023-09-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_react_date_of_birth_alter_react_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('admin_email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('content', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('admin_email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50, null=True)),
                ('organization', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.DeleteModel(
            name='React',
        ),
    ]