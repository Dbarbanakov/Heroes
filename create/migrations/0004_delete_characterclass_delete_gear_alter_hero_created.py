# Generated by Django 4.1.5 on 2023-01-12 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0003_alter_hero_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CharacterClass',
        ),
        migrations.DeleteModel(
            name='Gear',
        ),
        migrations.AlterField(
            model_name='hero',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 17, 19, 51, 35593)),
        ),
    ]
