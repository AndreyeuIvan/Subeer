# Generated by Django 3.0.2 on 2020-04-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_episode_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='url',
            field=models.TextField(),
        ),
    ]
