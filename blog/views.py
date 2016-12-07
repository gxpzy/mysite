from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog
# Create your views here.


def index(request):
    latest_blog_list = Blog.objects.all()
    template = loader.get_template('blogs/index.html')
    context = {
        'latest_blog_list': latest_blog_list,
    }
    return HttpResponse(template.render(context, request))