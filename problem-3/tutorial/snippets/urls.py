from django import urls
from rest_framework import urlpatterns as patterns
from snippets import views

urlpatterns = [
    urls.path("snippets/", views.SnippetList.as_view()),
    urls.path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
    urls.path("users/", views.UserList.as_view()),
    urls.path("users/<int:pk>/", views.UserDetail.as_view()),
]

"""
urlpatterns = [
    urls.path("snippets/", views.snippet_list),
    urls.path("snippets/<int:pk>/", views.snippet_detail),
]
"""
urlpatterns = patterns.format_suffix_patterns(urlpatterns)

urlpatterns += [
    urls.path('api-auth/', urls.include('rest_framework.urls')),
]
