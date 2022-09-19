from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('snippets.urls')),
    path('admin/', admin.site.urls),
]

# 로그인 화면
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]