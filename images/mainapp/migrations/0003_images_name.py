# Generated by Django 3.0.3 on 2020-06-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200623_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default='No Name', max_length=100),
            preserve_default=False,
        ),
    ]
