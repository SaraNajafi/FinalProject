# Generated by Django 3.2.19 on 2023-06-14 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230614_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
    ]