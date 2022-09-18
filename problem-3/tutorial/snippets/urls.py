from django import urls
from rest_framework import urlpatterns as patterns
from rest_framework import renderers
from rest_framework import routers
from snippets import views


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippets")
router.register(r'users', views.UserViewSet, basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    urls.path('', urls.include(router.urls)),
]
