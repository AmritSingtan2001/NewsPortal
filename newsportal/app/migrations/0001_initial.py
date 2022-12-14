# Generated by Django 4.0.5 on 2022-07-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('1', 'General'), ('2', 'Lifestyle'), ('3', 'Travel'), ('4', 'Fashion'), ('5', 'Sports'), ('6', 'Technology')], default='1', max_length=50)),
                ('headline', models.CharField(max_length=150)),
                ('short_description', models.TextField()),
                ('content', models.TextField()),
                ('images', models.ImageField(upload_to='newsimage')),
                ('reporter', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('1', 'Published'), ('2', 'Unpublished')], default='2', max_length=50)),
            ],
        ),
    ]
