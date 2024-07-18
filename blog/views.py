from django.shortcuts import render
from .models import Post

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'search.html', {'posts': posts})
