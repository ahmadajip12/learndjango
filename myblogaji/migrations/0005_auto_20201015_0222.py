# Generated by Django 2.2.16 on 2020-10-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogaji', '0004_auto_20201014_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
