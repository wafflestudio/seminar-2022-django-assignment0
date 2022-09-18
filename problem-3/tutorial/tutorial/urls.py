from django import urls
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    urls.path("", urls.include(router.urls)),
    urls.path("", urls.include("snippets.urls")),
    urls.path(
        "api-auth/", urls.include("rest_framework.urls", namespace="rest_framework")
    ),
]
