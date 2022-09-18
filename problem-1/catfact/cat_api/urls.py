from django.urls import path
from .apiviews import CatfactList, CatfactDetail, UserCreate, LoginView

app_name = 'catfact'

urlpatterns = [
    path('', CatfactList.as_view(), name='index'),
    path('<int:pk>/', CatfactDetail.as_view(), name='detail'),
    path('users/', UserCreate.as_view(), name="user_create"),
    path('login/', LoginView.as_view(), name="login"),
]