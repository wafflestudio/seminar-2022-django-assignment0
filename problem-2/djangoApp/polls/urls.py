from django.urls import path

from . import views

# URLconf에 이름공간 추가해 django가 {% url %} 탬플릿태그
# 사용해 어떤 앱의 뷰에서 url 생성할지 알 수 있게 해줌.
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]