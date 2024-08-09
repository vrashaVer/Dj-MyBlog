from django.urls import path
import blog.views as  blog_views

urlpatterns = [
    path("",blog_views.post_list,name="post_list"),
    path("post/<int:post_id>/",blog_views.post_detail,name='post_detail'),
    path('author/<int:author_id>/',blog_views.posts_by_author,name='posts_by_author'),
]