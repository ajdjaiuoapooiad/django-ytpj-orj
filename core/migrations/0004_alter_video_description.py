# Generated by Django 4.2 on 2024-11-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_video_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]