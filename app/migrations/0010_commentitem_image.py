# Generated by Django 4.0 on 2022-07-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_blogitem_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentitem',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
