# Generated by Django 3.0.5 on 2020-04-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]