# Generated by Django 2.2.5 on 2020-03-16 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
    ]
