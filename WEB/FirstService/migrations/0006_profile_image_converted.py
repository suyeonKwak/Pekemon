# Generated by Django 3.2.8 on 2021-11-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstService', '0005_alter_result_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_converted',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]