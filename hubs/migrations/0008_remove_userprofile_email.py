# Generated by Django 5.0.1 on 2024-01-14 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0007_alter_userprofile_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
