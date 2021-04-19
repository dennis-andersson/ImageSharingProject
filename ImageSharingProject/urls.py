"""ImageSharingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import login_view, logout_view, signup_view, profile_view
from images.views import * #images_post_view, images_browse_view, images_search_view, images_list_view, images_uploads_view, image_upload_view, welcome_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_view, name='welcome'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('upload/', image_upload_view, name='image_upload'),
    path('uploads/', images_uploads_view, name='image_uploads'),
    path('list/', images_list_view, name='images_list'),
    path('browse/', images_browse_view, name='image_browse'),
    path('search/', images_search_view, name='image_search'),
    path('profile/', profile_view, name='user_profile'),
]
