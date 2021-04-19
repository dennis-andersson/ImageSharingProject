from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


def get_file_path(instance, filename):
    now = datetime.now()
    return os.path.join('images', f'{now.year}/{now.month}/{now.day}/', filename)


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    upload_date = models.DateTimeField(default=datetime.now)
    file = models.ImageField(upload_to=get_file_path, blank=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file_path):
            os.remove(instance.file_path)


@receiver(pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).file
    except sender.DoesNotExist:
        return False

    new_file = instance.file
    if not new_file == old_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


