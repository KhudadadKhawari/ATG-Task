from unicodedata import category
from django.shortcuts import render
from .models import Blog
from account.models import User
from django.views.generic import ListView, DetailView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


method_decorator(login_required, name='dispatch')
class MyBlogs(ListView):
    model = Blog
    template_name = 'blog/my_blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


method_decorator(login_required, name='dispatch')
class BlogListView(View):
    context = {
        'title': 'Blog',
        'active_nav': 'blog',
    }
    def get(self, request, *args, **kwargs):
        try:
            if kwargs['category']:
                category = kwargs['category']
                blogs = Blog.objects.filter(category=category, is_draft=False)
        except:
            blogs = Blog.objects.filter(is_draft=False)
        covid19_cat = blogs.filter(category='Covid19')
        heart_disease_cat = blogs.filter(category='Heart Disease')
        mental_health_cat = blogs.filter(category='Mental Health')
        immunization_cat = blogs.filter(category='Immunization')
        self.context['covid19_cat'] = covid19_cat
        self.context['heart_disease_cat'] = heart_disease_cat
        self.context['mental_health_cat'] = mental_health_cat
        self.context['immunization_cat'] = immunization_cat

        return render(request, 'blog/blog_list.html', self.context)



method_decorator(login_required, name='dispatch')
class BlogDetailView(View):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context = {
        'active_nav': 'blog',
    }

    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk, is_draft=False)
        self.context['blog'] = blog
        self.context['title'] = blog.title
        return render(request, self.template_name, self.context)