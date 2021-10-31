# Generated by Django 3.2.7 on 2021-10-29 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('desc', models.TextField()),
                ('cjoin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=256)),
                ('grp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='signlog.groups')),
            ],
        ),
    ]