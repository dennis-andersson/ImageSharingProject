# Generated by Django 3.2 on 2021-04-20 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_delete_savedimage'),
        ('images', '0002_auto_20210420_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SavedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='images.image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
    ]