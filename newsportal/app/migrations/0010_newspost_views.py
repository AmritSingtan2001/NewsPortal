# Generated by Django 4.0.5 on 2022-08-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_weeklytopnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
