# Generated by Django 3.1.2 on 2020-10-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='abv',
            field=models.CharField(blank=True, choices=[('Below_10', '>10%'), ('10-20', '10% - 20%'), ('20-40', '20% - 40%'), ('40-60', '40% -  60%'), ('Above 60', '60%<')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='brand',
            field=models.CharField(blank=True, choices=[('Tuborg', 'TUBORG'), ('Nepal_ice', 'NEPAL ICE')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='country_of_origin',
            field=models.CharField(blank=True, choices=[('NP', 'Nepal'), ('IND', 'India')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beer',
            name='volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beer',
            name='category',
            field=models.CharField(choices=[('Large', 'LARGE'), ('Ale', 'ALE'), ('Stout', 'STOUT')], max_length=200),
        ),
    ]