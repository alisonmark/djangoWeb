# Generated by Django 2.0.6 on 2018-06-18 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Phone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pubDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
