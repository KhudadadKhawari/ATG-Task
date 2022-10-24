from django.urls import path
from .views import MyBlogs, BlogListView, BlogDetailView, blog_delete, publish_blog, update_blog


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<category>/', BlogListView.as_view(), name='blog_list'),
    path('my_blogs/all', MyBlogs.as_view(), name='my_blogs'),
    path('single/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('single/<int:pk>/publish', publish_blog, name='publish_blog'),
    path('sinlge/delete/<int:pk>/', blog_delete, name='blog_delete'),
    path('single/update/<int:pk>/', update_blog, name='update_blog'),
]