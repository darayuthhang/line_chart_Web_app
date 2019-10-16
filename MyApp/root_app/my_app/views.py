from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from threading import Timer

from .forms import UserRegisterForm
from .container import get_json
import json, random
import time
from threading import Thread


# Create your views here.
def index(request):
    # create object container
    Container = get_json()
    # user data dictionary for javascript, user1 , javascript_Datauser 2.
    User = Container.getUser()

    def first_thread():
        data_user_images = []

        data_user_images.append(Container.getUsername())
        data_user_images.append(Container.getTotalLikesOfCoverPhoto())
        data_user_images.append(Container.getTotalLikesOfProfile())
        return data_user_images

    data_user_image = first_thread()
    username = json.dumps(data_user_image[0])
    total_likes_of_profile = json.dumps(data_user_image[1])
    total_likes_of_cover_photo = json.dumps(data_user_image[2])
    if request.method == 'GET':
        # create user dict to store data
        # convert data to json
        # data_user_image = first_thread()
        # username = json.dumps(data_user_image[0])
        # total_likes_of_profile = json.dumps(data_user_image[1])
        # total_likes_of_cover_photo = json.dumps(data_user_image[2])
        return render(request, "my_app/index.html", {
            'username': username,
            'total_likes_of_profile': total_likes_of_profile,
            'total_likes_of_cover_photo': total_likes_of_cover_photo,
            'User': User,
        })
    elif request.method == "POST":

        return render(request, "my_app/index.html", {
            'username': username,
            'total_likes_of_profile': total_likes_of_profile,
            'total_likes_of_cover_photo': total_likes_of_cover_photo,
            'User': User,
        })

# add the decorating so that
# the log out require the login
# to log out
@login_required
def user_logout(request):
    logout(request)
    return redirect('/homepage/')


def register(request):
    # create object to holder form object
    # so that it is easy to read
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ## get the password of ther user
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/homepage/')
    else:
        form = UserRegisterForm()
    return render(request, "my_app/register.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            if user is not None:
                # send the auten pass and username
                # to the build function in login library
                login(request, user)
                return redirect('/homepage/')
            else:
                return HttpResponse("account not active")
        else:
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalud")
    else:
        # get method and return the route route
        return render(request, 'my_app/login.html')
