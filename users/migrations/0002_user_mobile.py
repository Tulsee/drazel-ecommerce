# Generated by Django 3.1.2 on 2020-10-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(blank=True, default=0, unique=True),
            preserve_default=False,
        ),
    ]
