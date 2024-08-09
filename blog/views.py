from django.shortcuts import render
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list":posts
    }
    return render(
        request,
        template_name="blog/post_list.html",
        context=context
    )
