# Generated by Django 3.2.4 on 2022-10-02 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_alter_lead_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='link_lp',
            new_name='landing_page',
        ),
    ]