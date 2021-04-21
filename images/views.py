from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image, SavedImage
from django.contrib.auth.models import User
from utils import get_image_dict, get_images_dict


def image_save_view(request, id):
    n = len(SavedImage.objects.filter(user_id=request.user.id).filter(image_id=id))
    if n == 0:
        image = get_object_or_404(Image, pk=id)
        saved_image = SavedImage(user=request.user, image=image)
        saved_image.save()
    return redirect('/post/' + str(id))

def image_unsave_view(request, id):
    saved_image = SavedImage.objects.filter(user_id=request.user.id).filter(image_id=id)
    if len(saved_image) > 0:
        saved_image = saved_image[0]
        saved_image.delete()
    return redirect('/post/' + str(id))

def images_post_view(request, id):
    saved = len(SavedImage.objects.filter(user_id=request.user.id).filter(image_id=id)) > 0
    image = get_image_dict(get_object_or_404(Image, pk=id))
    uploader = image['uploader'].id == request.user.id
    return render(request, 'image_post.html', {'image': image, 'user': request.user, 'saved': saved, 'uploader': uploader})

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

    return render(request, 'images_search.html', {'images': images, 'users': searched_users, 'query': query, 'user': request.user})

def images_list_view(request):
    images = Image.objects.all().order_by('-upload_date')
    return render(request, 'images_list.html', {'images': images, 'user': request.user})

def images_uploads_view(request):
    images = get_images_dict(Image.objects.filter(uploader_id=request.user.id)) #.order_by('-upload_date')
    return render(request, 'images_list.html', {'images': images})

def images_profile_uploads_view(request, id):
    images = get_images_dict(Image.objects.filter(uploader_id=request.user.id))
    return render(request, 'images_list.html', {'images': images})

def image_upload_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.uploader = request.user
            image.save()
            return redirect('/profile/' + str(request.user.id) + '/uploads/')

    return render(request, 'image_upload.html', {'form': form})

def images_edit_view(request, id):
    image = get_object_or_404(Image, pk=id)
    if image.uploader.id == request.user.id:
        image = get_image_dict(image)
        return render(request, 'image_edit.html', {"image": image, 'user': request.user})
    else:
        return redirect('/post/' + str(id))

def images_delete_view(request, id):
    image = get_object_or_404(Image, pk=id)
    if image:
        if request.user.id == image.uploader.id:
            image.delete()
            return redirect('/profile/uploads/')
        else:
            return redirect('/post/' + str(id))

def welcome_view(request):
    return render(request, "welcome.html", {'user': request.user})
