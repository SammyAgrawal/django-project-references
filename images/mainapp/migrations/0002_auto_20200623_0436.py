# Generated by Django 3.0.3 on 2020-06-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.ImageField(upload_to='pics'),
        ),
    ]