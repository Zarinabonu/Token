from django.urls import path, include

urlpatterns = [
    path('post/', include('api.post.urls')),
]