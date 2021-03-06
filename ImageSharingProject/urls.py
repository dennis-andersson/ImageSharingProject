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
from user.views import login_view, logout_view, signup_view, profile_view, show_profile_view
from images.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_view, name='welcome'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('upload/', image_upload_view, name='image_upload'),
    path('profile/uploads/', images_uploads_view, name='image_uploads'),
    path('profile/<int:id>/uploads/', images_profile_uploads_view, name='image_profile_uploads'),
    path('post/<int:id>', images_post_view, name='image_post'),
    path('post/edit/<int:id>', images_edit_view, name='image_edit'),
    path('post/delete/<int:id>', images_delete_view, name='image_delete'),
    path('list/', images_list_view, name='images_list'),
    path('browse/', images_browse_view, name='images_browse'),
    path('search/', images_search_view, name='image_search'),
    path('save/<int:id>', image_save_view, name='image_save'),
    path('unsave/<int:id>', image_unsave_view, name='image_unsave'),
    path('profile/', profile_view, name='user_profile'),
    path('profile/<int:id>', profile_view, name='user_profile'),
    path('showprofile/<int:id>', show_profile_view, name='show_profile'),
]
