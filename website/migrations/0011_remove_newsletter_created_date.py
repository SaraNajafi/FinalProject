# Generated by Django 3.2.19 on 2023-06-15 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_newsletter_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='created_date',
        ),
    ]
