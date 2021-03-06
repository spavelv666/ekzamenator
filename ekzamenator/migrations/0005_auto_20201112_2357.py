# Generated by Django 3.1.2 on 2020-11-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekzamenator', '0004_auto_20201112_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AddField(
            model_name='users',
            name='url',
            field=models.SlugField(default=2, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]
