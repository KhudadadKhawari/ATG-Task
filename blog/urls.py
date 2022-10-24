from django.urls import path
from .views import MyBlogs, BlogListView, BlogDetailView


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<category>/', BlogListView.as_view(), name='blog_list'),
    path('my_blogs/', MyBlogs.as_view(), name='my_blogs'),
    path('single/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]