# Generated by Django 3.2.19 on 2023-06-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=31, null=True),
        ),
    ]
