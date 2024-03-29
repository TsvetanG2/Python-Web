# Generated by Django 4.2.7 on 2024-02-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Album Name'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=30, verbose_name='Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('JAZZ MUSIC', 'Jazz Music'), ('R&B MUSIC', 'R&B Music'), ('ROCK MUSIC', 'Rock Music'), ('COUNTRY MUSIC', 'Country Music'), ('DANCE MUSIC', 'Dance Music'), ('HIP HOP MUSIC', 'Hip Hop Music'), ('OTHER', 'Other')], max_length=30, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
    ]
