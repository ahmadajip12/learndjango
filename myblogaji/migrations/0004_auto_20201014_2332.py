# Generated by Django 2.2.16 on 2020-10-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogaji', '0003_auto_20201014_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='pos',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='myblogaji.Tag'),
        ),
    ]