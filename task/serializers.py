from django.contrib.auth.models import User
from .models import Task
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'is_done', 'user']

class UserSerializerTask(serializers.HyperlinkedModelSerializer):
    tsks = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['username', 'email', 'tsks']
