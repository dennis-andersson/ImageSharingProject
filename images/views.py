from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image


def images_post_view(request):
    images = Image.objects.all()
    return render(request, 'images_list.html', {'images': images, 'userkeys': str(dir(request.user))})

def images_browse_view(request):
    images = Image.objects.all()
    return render(request, 'images_browse.html', {'images': images, 'userkeys': str(dir(request.user))})

def images_search_view(request):
    images = Image.objects.all()
    return render(request, 'images_browse.html', {'images': images, 'userkeys': str(dir(request.user))})

def images_list_view(request):
    images = Image.objects.all()
    return render(request, 'images_list.html', {'images': images, 'userkeys': str(dir(request.user))})

def images_uploads_view(request):
    return render(request, 'images_uploads.html', {})

def image_upload_view(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            redirect('images_list')

    return render(request, 'image_upload.html', {'form': form})

def welcome_view(request):
    return render(request, "welcome.html", {})
