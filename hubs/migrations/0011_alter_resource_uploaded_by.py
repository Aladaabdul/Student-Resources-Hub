# Generated by Django 5.0.1 on 2024-01-18 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0010_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hubs.userprofile'),
            preserve_default=False,
        ),
    ]
