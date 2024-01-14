# Generated by Django 4.1.1 on 2024-01-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='course_name',
            new_name='language1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='institute',
            new_name='language2',
        ),
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='language3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
