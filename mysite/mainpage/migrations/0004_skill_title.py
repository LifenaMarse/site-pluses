# Generated by Django 4.1.5 on 2023-01-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_rename_skills_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
