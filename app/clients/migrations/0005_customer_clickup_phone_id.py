# Generated by Django 3.2.4 on 2022-10-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20221003_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='clickup_phone_id',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
