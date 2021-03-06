# Generated by Django 3.2.10 on 2022-01-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('site', models.TextField()),
                ('is_rented', models.BooleanField(default=False)),
                ('lessor_number', models.IntegerField(default='...')),
                ('lessor_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
