# Generated by Django 3.1.4 on 2020-12-16 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapi', '0002_auto_20201215_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_stars', to='youtubeapi.video'),
        ),
    ]