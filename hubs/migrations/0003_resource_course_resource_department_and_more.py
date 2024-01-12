# Generated by Django 5.0.1 on 2024-01-12 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0002_rename_username_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hubs.course'),
        ),
        migrations.AddField(
            model_name='resource',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hubs.department'),
        ),
        migrations.AddField(
            model_name='resource',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hubs.user'),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
