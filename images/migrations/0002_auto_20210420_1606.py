# Generated by Django 3.2 on 2021-04-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='file',
            new_name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
