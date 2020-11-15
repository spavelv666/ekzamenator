# Generated by Django 3.1.2 on 2020-11-11 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekzamenator', '0002_uch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uch',
            options={'verbose_name': 'Участок', 'verbose_name_plural': 'Участки'},
        ),
        migrations.AddField(
            model_name='uch',
            name='pp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekzamenator.pp', verbose_name='Дроизводственое подраздилени'),
        ),
        migrations.AlterField(
            model_name='uch',
            name='shu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekzamenator.shu', verbose_name='Шахто-управление'),
        ),
    ]