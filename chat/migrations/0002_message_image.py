# Generated by Django 2.0 on 2022-10-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
