# Generated by Django 5.1.7 on 2025-03-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_product_user_alter_socialpost_generated_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('caption', models.TextField()),
                ('hashtags', models.TextField()),
                ('schedule_time', models.DateTimeField()),
                ('is_posted', models.BooleanField(default=False)),
            ],
        ),
    ]
