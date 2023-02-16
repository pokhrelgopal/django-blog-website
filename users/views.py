from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from .models import Profile


def signupUser(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        passwordOne = request.POST.get("password1")
        passwordTwo = request.POST.get("password2")

        if (username and passwordOne and passwordTwo):
            if (len(passwordOne) < 8):
                error = "password too short"
            if (len(passwordOne) >= 8):
                if (passwordOne != passwordTwo):
                    error = "password mismatch"
                else:
                    existing_user = User.objects.filter(username=username)
                    if existing_user.exists():
                        error = "username already exists"
                    else:
                        my_user = User.objects.create_user(
                            username=username,
                            password=passwordOne,
                        )
                        my_user.save()
                        return redirect('login')

    context = {
        'error': error
    }
    return render(request, 'users/signup.html', context)


from django.contrib.auth.decorators import login_required

@login_required
def addInfo(request):
    profile = get_object_or_404(Profile,user = request.user)
    if request.method == "POST":
        profile.name = request.POST.get('fullname')
        profile.email = request.POST.get('emailaddress')
        profile.short_intro = request.POST.get('shortintro')
        profile.bio = request.POST.get('bio')
        profile.profile_image = request.FILES.get('profilepicture')
        profile.save()
        return redirect('profile')
    
    context = {
        'profile':profile
    }
    return render(request, 'users/add-info.html',context)



def loginUser(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "incorrect details"
    context = {
        'error': error
    }

    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def addBlog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        blog_post = BlogPost()
        blog_post.author = request.user
        blog_post.title = title
        blog_post.content = description
        blog_post.featured_image = image
        blog_post.save()

        return redirect('home')

    return render(request, 'users/addForm.html')


@login_required(login_url='login')
def profilePage(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    posts = BlogPost.objects.filter(author=user).order_by("-created_date")
    context = {
        'profile':profile,
        'posts': posts
    }
    return render(request, 'users/profile-page.html', context)



def updateBlog(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.featured_image = request.FILES.get('image')
        post.save()
        return redirect('profile')
    context = {
        'post': post
    }
    return render(request, 'users/edit-post.html', context)


def deleteBlog(request, id):
    post = get_object_or_404(BlogPost, id=id)
    creator = post.author.username
    if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:
        post.delete()
        return redirect('profile')
    context = {
        'post': post
    }
    return render(request, 'users/delete-post.html', context)
