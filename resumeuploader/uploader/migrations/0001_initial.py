# Generated by Django 4.2.7 on 2024-01-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=20)),
                ('pimage', models.ImageField(blank=True, upload_to='pimages')),
                ('rdoc', models.FileField(blank=True, upload_to='rdoc')),
            ],
        ),
    ]