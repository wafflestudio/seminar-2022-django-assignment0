from django import urls

from snippets import views

urlpatterns = [
    urls.path("snippets/", views.snippet_list),
    urls.path("snippets/<int:pk>/", views.snippet_detail),
]
