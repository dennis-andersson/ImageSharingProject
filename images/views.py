from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image
from django.contrib.auth.models import User
from utils import get_image_dict, get_images_dict


def images_post_view(request, id):
    image = get_image_dict(get_object_or_404(Image, pk=id))
    return render(request, 'image_post.html', {'image': image, 'user': request.user})

def images_browse_view(request):
    all_images = Image.objects.all().order_by('-upload_date')
    images = get_images_dict(all_images)
    return render(request, 'images_browse.html', {'images': images, 'user': request.user})

def images_search_view(request):
    query = request.GET.get('q')
    if query is not None and query != "":
        searched_titles = Image.objects.filter(title__contains=query)
        searched_descriptions = Image.objects.filter(description__contains=query)
        searched_images = searched_titles | searched_descriptions
        searched_users = User.objects.filter(username__contains=query)
        images = get_images_dict(searched_images)

    return render(request, 'images_list.html', {'images': images, 'user': request.user})

def images_list_view(request):
    images = Image.objects.all().order_by('-upload_date')
    return render(request, 'images_list.html', {'images': images, 'user': request.user})

def images_uploads_view(request):
    images = Image.objects.filter(user=request.user) #.order_by('-upload_date')
    return render(request, 'images_uploads.html', {'images': images})

def image_upload_view(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.uploader = request.user
            image.thumbnail = image.get_thumbnail_filename()
            image.save()
            form = ImageForm()
            redirect('/profile/' + request.user.id + '/uploads')

    return render(request, 'image_upload.html', {'form': form})

def images_edit_view(request, id):
    image = Image.objects.filter(id=id)
    Image.objects.order_by(upload_date)
    return render(request, 'image_edit.html', {"image": image, 'user': request.user})

def images_delete_view(request, id):
    image = get_object_or_404(Image, pk=id)
    if image:
        if request.user.id == image.uploader.id:
            image.delete()
            redirect('/profile/uploads')
        else:
            pass

def welcome_view(request):
    return render(request, "welcome.html", {'user': request.user})
