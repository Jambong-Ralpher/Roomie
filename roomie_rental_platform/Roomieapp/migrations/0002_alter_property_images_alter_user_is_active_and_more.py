# Generated by Django 5.1.4 on 2024-12-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roomieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.ImageField(upload_to='property_images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
