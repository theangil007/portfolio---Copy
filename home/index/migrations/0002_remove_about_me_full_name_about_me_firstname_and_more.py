# Generated by Django 4.1.1 on 2023-12-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_me',
            name='full_name',
        ),
        migrations.AddField(
            model_name='about_me',
            name='firstname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about_me',
            name='lastname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
