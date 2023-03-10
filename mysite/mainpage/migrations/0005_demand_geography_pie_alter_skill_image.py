# Generated by Django 4.1.5 on 2023-01-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_skill_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Pie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
