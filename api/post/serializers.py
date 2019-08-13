from rest_framework.serializers import ModelSerializer
from post.models import Post, Files
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import random
import string

from untitled1 import settings
from user.models import Profile


class CreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description')

    def create(self, validated_data):

        request = self.context['request']
        p = Post(**validated_data)
        for file in request.FILES.getlist('file'):
            f = Files.objects.create(file_user=p, file=file)

        title = self.context['request'].data.get('title')
        description = self.context['request'].data.get('description')
        password = ''
        token = ''
        uname = request.data.get('username')
        uemail = request.data.get('email')
        if uname:
            password = randomstring(stringLength=5)
            token = randomstring(stringLength=10)
            u = User.objects.create(username=uname, email=uemail)
            u.set_password(password)
            pro = Profile.objects.create(user=u)
            pro.activation_token = token
            pro.save()
            u.save()
            p.poster = u
            p.save()
        body='Title:'+title+'\n'+'Description:'+description+'\n'+'username:'+uname+'\npassword:'+str(password)+'\nActivation url:http://127.0.0.1:8000/user/activate/'+str(token)
        msg = EmailMessage(
            title,
            body,
            settings.EMAIL_HOST_USER,
            ['ergash1994@gmail.com'])
        msg.send()
        print(request.data)
        return p

def randomstring(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))