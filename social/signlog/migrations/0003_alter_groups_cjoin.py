# Generated by Django 3.2.7 on 2021-10-29 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlog', '0002_groups_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='cjoin',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
