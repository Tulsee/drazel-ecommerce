# Generated by Django 3.1.2 on 2020-10-24 15:54

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201024_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='picture',
            field=models.ImageField(default=0, upload_to=products.models.beer_images),
            preserve_default=False,
        ),
    ]