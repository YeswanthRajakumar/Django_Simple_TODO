# Generated by Django 3.0.5 on 2020-04-10 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0009_remove_notes_description'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]