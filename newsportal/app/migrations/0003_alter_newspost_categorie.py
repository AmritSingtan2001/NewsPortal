# Generated by Django 4.0.5 on 2022-07-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_newspost_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='categorie',
            field=models.CharField(choices=[('General', 'General'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Fashion', 'Fashion'), ('Sports', 'Sports'), ('Technology', 'Technology')], default='General', max_length=50),
        ),
    ]
