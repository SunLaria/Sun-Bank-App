# Generated by Django 4.2.7 on 2024-06-19 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_api', '0002_rename_to_account_transitions_to_account_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transitions',
            new_name='Transition',
        ),
    ]
