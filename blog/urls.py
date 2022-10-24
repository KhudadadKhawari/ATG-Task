from django.urls import path
from .views import MyBlogs, BlogListView, BlogDetailView, blog_delete, publish_blog, update_blog
from .test_data import create_blog

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'), # all blogs
    path('<category>/', BlogListView.as_view(), name='blog_list'), # blogs by category
    path('my_blogs/all', MyBlogs.as_view(), name='my_blogs'), # all blogs by logged_in user
    path('single/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  # single blog
    path('single/<int:pk>/publish', publish_blog, name='publish_blog'), # publish drafted blog
    path('sinlge/delete/<int:pk>/', blog_delete, name='blog_delete'), # delete blog
    path('single/update/<int:pk>/', update_blog, name='update_blog'), # update blog

    # test data
    path('test-data/add', create_blog, name='create_blog'), # create test data blog post
]