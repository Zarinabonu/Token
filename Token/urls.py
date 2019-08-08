from django.contrib import admin
from django.urls import path
# from .views import login, sample_api
from Token import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello')
    # path('api/login', login),
    # path('api/sampleapi', sample_api),
]