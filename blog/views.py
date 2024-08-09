from django.shortcuts import render, get_object_or_404
from blog.models import Post,Author


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
def post_detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    comments = post.comment_set.all()
    context = {
        "post":post,
        "comments":comments
    }
    return render(
        request, 
        template_name='blog/post_detail.html',
        context=context
        )

def posts_by_author(request,author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author)
    context =  {
        'author': author, 
        'posts': posts
        }
    return render(
        request, 
        template_name='blog/posts_by_author.html', 
        context=context
        )