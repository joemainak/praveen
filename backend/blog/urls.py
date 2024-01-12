from django.urls import path
from .views import BlogView, PublicBlogView

urlpatterns = [
    path('post/', BlogView.as_view(), name='blog'),
    path('blog_posts/', PublicBlogView.as_view(), name='blogs')
]