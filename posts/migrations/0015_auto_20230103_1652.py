# Generated by Django 3.2.9 on 2023-01-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20230102_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofiledetails',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='ProfilePhotos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
