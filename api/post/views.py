
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post
from .serializers import CreateSerializer

class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreateSerializer
