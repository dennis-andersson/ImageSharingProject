from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete, pre_save
from django.contrib.auth.models import User
from user.models import UserProfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.dispatch import receiver
from PIL import Image as PIL_Image
import glob, os


def get_file_path(instance, filename):
    now = datetime.now()
#    path = '/'.join(['', 'static', 'uploads', instance.user.username, f'{now.year}-{now.month}-{now.day}', filename])
    path = os.path.join('static', 'uploads', instance.uploader.username, f'{now.year}-{now.month}-{now.day}', filename)
    return path


class Image(models.Model):
    uploader = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    upload_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to=get_file_path, blank=True)
    thumbnail = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

    def get_file_format(self, extension):
        extension = extension.lower()
        if extension in ['.jpg', '.jpeg']:
            return "JPEG"
        elif extension == '.png':
            return "PNG"
        elif extension == '.gif':
            return "GIF"

    def get_thumbnail_filename(self):
        filename = self.image.url
        name, ext = os.path.splitext(filename)
        thumbnail_filename = name + "-thumbnail" + ext
        return thumbnail_filename

    def create_thumbnail(self):
        filename = self.image.path
        thumbnail_filename = self.get_thumbnail_filename()
        size = 128, 128
        ext = os.path.splitext(filename)[1]

        with PIL_Image.open(filename) as im:
            im.thumbnail(size)
            im.save(thumbnail_filename, self.get_file_format(ext))


    def save(self):
#        self.thumbnail = self.get_thumbnail_filename()
        super(Image, self).save()
        self.create_thumbnail()

    class Meta:
        ordering = ['-id']


class SavedImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)


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


