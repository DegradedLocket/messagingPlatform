# Generated by Django 4.0.3 on 2022-04-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='userFrom',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
