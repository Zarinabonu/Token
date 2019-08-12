from django.contrib.auth import authenticate
from django.http import response
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import Profile


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, Word!'}
        return Response(content)
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None :
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error':'Invalid Credentails'},
                        status=HTTP_404_NOT_FOUND)
    token, _= Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

class AccountActivateView(View):
    def get(self, request, *args, **kwargs):
        print(self.kwargs['q'])
        profile = Profile.objects.get(activation_token=self.kwargs['q'])
        profile.user.is_active = True
        profile.user.save()
        return render(self.request, 'te.html')

class MainHtml(View):
    def get(self, request):
        return render(request, '')

# Create your views here.
