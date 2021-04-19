from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm


def profile_view(request):
    return render(request, "user-profile.html", {})

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





