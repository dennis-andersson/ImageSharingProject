from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from images.models import Image, SavedImage
from django.contrib.auth.models import User
from utils import get_image_dict, get_images_dict


def show_profile_view(request, id):
    images = get_images_dict(Image.objects.filter(uploader_id=id))
    profile = get_object_or_404(User, pk=id)
    return render(request, "show-profile.html", {'images': images, 'profile': profile})

def profile_view(request, id):
    savedimages = SavedImage.objects.filter(user_id=request.user.id)
    if len(savedimages) > 0:
        savedimages = get_images_dict([si.image for si in savedimages])
    myimages = Image.objects.filter(uploader_id=request.user.id)
    if len(myimages) > 0:
        myimages = get_images_dict(myimages)
    return render(request, "user-profile.html", {'savedimages': savedimages, 'myimages': myimages})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and or password', 'username': username})
    return render(request, "login.html", {})


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, 'signup.html', {'form': form, 'error': 'Could not login user'})
    return render(request, 'signup.html', {'form': form})





