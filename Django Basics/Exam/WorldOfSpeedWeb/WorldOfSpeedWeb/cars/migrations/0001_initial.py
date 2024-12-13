# Generated by Django 4.2.7 on 2024-02-24 08:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('RALLY', 'Rally'), ('OPEN-WHEEL', 'Open-wheel'), ('KART', 'Kart'), ('DRAG', 'Drag'), ('OTHER', 'Other')], max_length=10, verbose_name='Type')),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Model')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('image_url', models.URLField(default='https://...', error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, unique=True, verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)], verbose_name='Price')),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]