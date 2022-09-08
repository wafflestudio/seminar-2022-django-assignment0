from django import urls

from polls import views

app_name = "polls"
urlpatterns = [
    # urls.path("", views.index, name="index"),
    # urls.path("<int:question_id>/", views.detail, name="detail"),
    # urls.path("<int:question_id>/results/", views.results, name="results"),
    urls.path("", views.IndexView.as_view(), name="index"),
    urls.path("<int:question_id>/", views.DetailView.as_view(), name="detail"),
    urls.path("<int:question_id>/results/", views.ResultsView.as_view(), name="results"),
    urls.path("<int:question_id>/vote/", views.vote, name="vote"),
]
