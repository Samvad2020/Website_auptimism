# Generated by Django 3.0.7 on 2020-06-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auptimism_main', '0003_auto_20200620_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
