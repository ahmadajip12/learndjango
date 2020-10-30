# Generated by Django 2.2.16 on 2020-10-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogaji', '0002_command'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title']},
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tag', models.CharField(max_length=50)),
                ('pos', models.ManyToManyField(to='myblogaji.Post')),
            ],
            options={
                'ordering': ['name_tag'],
            },
        ),
    ]