# Generated by Django 4.2.7 on 2024-04-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
