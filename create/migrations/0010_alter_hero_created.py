# Generated by Django 4.1.5 on 2023-01-16 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0009_alter_hero_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 16, 21, 39, 11, 651409)),
        ),
    ]