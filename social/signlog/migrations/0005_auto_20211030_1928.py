# Generated by Django 3.2.7 on 2021-10-30 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signlog', '0004_auto_20211030_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='grp',
            new_name='Group',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='message',
            new_name='Message',
        ),
    ]
