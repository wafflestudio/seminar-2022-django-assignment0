from django import urls

from polls import views

urlpatterns = [
    urls.path("", views.index, name="index"),
]
