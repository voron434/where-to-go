# Generated by Django 3.2.4 on 2021-06-16 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description_short', models.TextField(blank=True, max_length=500)),
                ('description_long', models.TextField(blank=True)),
                ('coord_lng', models.FloatField(null=True)),
                ('coord_lat', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=None)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.place')),
            ],
        ),
    ]