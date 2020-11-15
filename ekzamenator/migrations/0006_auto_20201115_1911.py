# Generated by Django 3.1.2 on 2020-11-15 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekzamenator', '0005_auto_20201112_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='url',
        ),
        migrations.AlterField(
            model_name='users',
            name='pp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekzamenator.pp', verbose_name='Производственое подраздилени'),
        ),
    ]