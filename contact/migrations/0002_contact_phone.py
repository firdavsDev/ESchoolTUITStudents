# Generated by Django 5.0.4 on 2024-05-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='phone number'),
        ),
    ]
