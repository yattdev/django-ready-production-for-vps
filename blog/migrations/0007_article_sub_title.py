# Generated by Django 3.2.10 on 2021-12-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
