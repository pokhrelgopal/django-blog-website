from django.shortcuts import render
from . models import BlogPost


def index(request):
    posts = BlogPost.objects.all().order_by('-created_date')

    if request.method == "POST":
        search_data = request.POST.get('search-data')
        posts = BlogPost.objects.filter(title__icontains=search_data)

    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)



def blog(request, pk):
    singleBlog = BlogPost.objects.get(id=pk)
    return render(request, 'blog/blog-single-page.html', {'singleBlog': singleBlog})
