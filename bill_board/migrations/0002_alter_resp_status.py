# Generated by Django 4.1.1 on 2022-09-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resp',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Принято'),
        ),
    ]
