# Generated by Django 4.0 on 2022-07-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_commentitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='commentcount',
            field=models.IntegerField(default=0),
        ),
    ]
