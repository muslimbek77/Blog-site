from django.shortcuts import render
from requests import request
from post.models import Post
from rest_framework import generics, permissions
from .serializers import PostSerializer

# Create your views here.

def indexview(request):
    posts = Post.objects.all()[:12]
    
    q=request.GET.get('q')
    if q:
        posts = Post.objects.filter(title__icontains=q)
        return render(request,'index.html',{'results':posts})
    else:
        return render(request,'index.html',{'posts':posts})     


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()[:12]
    serializer_class = PostSerializer




            
        
    
    

