from django import http
from django.contrib.auth import models
from django.views.decorators import csrf
from rest_framework import (
    decorators,
    generics,
    mixins,
    parsers,
    permissions,
    renderers,
    response,
    reverse,
    status,
    views,
    viewsets,
)
from snippets import models as snippet_models
from snippets import permissions as snippet_permissions
from snippets import serializers


@decorators.api_view(["GET"])
def api_root(request, format=None):
    return response.Response(
        {
            "users": reverse.reverse("user-list", request=request, format=format),
            "snippets": reverse.reverse("snippet-list", request=request, format=format),
        }
    )


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = snippet_models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        snippet_permissions.IsOwnerOrReadOnly,
    ]

    @decorators.action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return response.Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
