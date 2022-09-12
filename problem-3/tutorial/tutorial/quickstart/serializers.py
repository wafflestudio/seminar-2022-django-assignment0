from django.contrib.auth.models import User, Group
from rest_framework import serializers


# we're using hyperlinked relations in this case with HyperlinkedModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']