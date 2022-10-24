from django.shortcuts import render, redirect
from .models import Blog, CATEGORIES
from account.models import User
from django.views.generic import ListView, DetailView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogForm


method_decorator(login_required, name='dispatch')
class MyBlogs(View):
    template_name = 'account/doctor-dashboard.html'
    context = {
        'title': 'My Blogs',
        'active_nav': 'dashboard',
        'dash_nav_active': 'my_blogs',
        'categories': CATEGORIES,
        'form': BlogForm(),
    }

    def get(self, request):
        self.context['blogs'] = Blog.objects.filter(author=request.user)
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Blog published successfully')
            return redirect('my_blogs')
        else:
            self.context['form'] = form
            messages.error(request, 'Blog not Saved')
            return render(request, self.template_name, self.context)



@login_required
def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        form.save()
        messages.success(request, 'Blog updated successfully')
        return redirect('my_blogs')
    else:
        messages.error(request, 'Blog not updated')
        return redirect('my_blogs')


@login_required
def publish_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if blog.author == request.user:
        blog.is_draft = False
        blog.save()
        messages.success(request, 'Blog published successfully')
        return redirect('my_blogs')
    else:
        messages.error(request, 'You are not authorized to publish this blog')
        return redirect('home')
        

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
        blog = Blog.objects.get(pk=pk)
        if blog.is_draft and request.user != blog.author:
            messages.error(request, "You don't have access to this blog")
            return redirect('blog_list')

        self.context['blog'] = blog
        self.context['title'] = blog.title
        return render(request, self.template_name, self.context)


@login_required
def blog_delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    if blog.author == request.user:
        blog.delete()
        messages.success(request, 'Blog deleted successfully', 'alert-success')
        return redirect('my_blogs')
