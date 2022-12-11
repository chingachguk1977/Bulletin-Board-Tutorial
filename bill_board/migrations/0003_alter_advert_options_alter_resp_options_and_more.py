# Generated by Django 4.1 on 2022-12-10 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bill_board', '0002_alter_resp_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'verbose_name': 'Advertisement', 'verbose_name_plural': 'Advertisements'},
        ),
        migrations.AlterModelOptions(
            name='resp',
            options={'verbose_name': 'Response', 'verbose_name_plural': 'Responses'},
        ),
        migrations.AlterField(
            model_name='advert',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Attachment'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('tanks', 'Tanks'), ('heals', 'Healers'), ('dd', "DD's"), ('traders', 'Traders'), ('givers', 'Quest Givers'), ('smiths', 'Smiths'), ('tanners', 'Tanners'), ('potions', 'Potion Makers'), ('spellcasters', 'Spell Casters')], default='tanks', max_length=12, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='text',
            field=models.TextField(verbose_name='Ad body'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Ad title'),
        ),
        migrations.AlterField(
            model_name='resp',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='resp',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Response Date'),
        ),
        migrations.AlterField(
            model_name='resp',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill_board.advert', verbose_name='Advertisement'),
        ),
        migrations.AlterField(
            model_name='resp',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Accepted'),
        ),
        migrations.AlterField(
            model_name='resp',
            name='text',
            field=models.TextField(verbose_name='Response body'),
        ),
    ]
