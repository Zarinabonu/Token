from django.contrib import admin
from django.urls import path
from .views import login
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.HelloView.as_view(), name='hello'),
    path('api/login', login),
    path('activate/<str:q>', views.AccountActivateView.as_view(), name='account-activate'),
    # path('api/sampleapi', sample_api),
]