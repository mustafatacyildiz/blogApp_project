from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from django.contrib.auth import logout, login, authenticate
from .forms import UserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile

# Create your views here.

def home(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')


def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, 'Register Successfull!')

            return redirect('home')

    context = {
        "form_user": form_user,
        "form_profile": form_profile
    }
    return render(request, 'users/register.html',context)


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password = password)

        user = form.get_user()

        if user:
            messages.success(request,'login successfull')
            login(request, user)
            return redirect('home')

    return render(request, 'users/user_login.html', {"form":form})


def profile(request):
    userform= UserForm(request.POST or None, instance = request.user)
    profileform = UserProfileForm(request.POST or None, instance = request.user.userprofile, files = request.FILES)
    
    # if request.method == "POST":
    #     form = UserProfileForm(request.POST, instance=user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("home")
    
    context = {
        "userform" : userform,
        "profileform": profileform
    }
    return render(request, "users/profile.html", context)



