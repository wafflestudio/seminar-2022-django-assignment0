from django.contrib.auth import models
from rest_framework import permissions, viewsets
from tutorial.quickstart import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows users to be viewed or edited.
    """

    queryset = models.User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows groups to be viewed or edited.
    """

    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
