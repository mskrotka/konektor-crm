# Generated by Django 3.2.4 on 2022-10-02 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20221002_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='lead_extend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.leadextend'),
        ),
    ]
