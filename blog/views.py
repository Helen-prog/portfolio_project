from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    blogs = Blog.objects.order_by('-date')  # самые свежие публикации 5 шт
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # pk - первичный ключ, ищется id под нужным номером,
    # если не получается возвращает ошибку 404
    return render(request, 'blog/details.html', {'blog': blog})
