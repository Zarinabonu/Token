from django.urls import path

from post.views import ListPost

urlpatterns = [
    path('', ListPost.as_view(), name='index'),
]