# Generated by Django 5.0.4 on 2024-04-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tg_username',
            field=models.CharField(max_length=100, verbose_name='telegram username with @'),
        ),
    ]
