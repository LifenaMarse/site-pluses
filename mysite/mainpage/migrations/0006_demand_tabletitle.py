# Generated by Django 4.1.5 on 2023-01-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_demand_geography_pie_alter_skill_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='tableTitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]