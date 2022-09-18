from rest_framework import generics, status, permissions
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication

from .models import Catfact
from .serializers import CatfactSerializer, UserSerializer

# catfact/
class CatfactList(generics.ListCreateAPIView):
    # get은 로그인 없이 가능
    # post는 로그인 없이 불가
    queryset = Catfact.objects.all()[:20]
    serializer_class = CatfactSerializer
    def post(self, request, *args, **kwargs):
        # 로그인 여부 확인
        if not request.user.is_authenticated:
            raise PermissionDenied("login required to post catfact.")
        return super().post(request, *args, **kwargs)
    
# catfact/<int:pk>/
class CatfactDetail(generics.RetrieveUpdateDestroyAPIView):
    # GET은 로그인 없이 가능
    # delete는 로그인 없이 불가능
    queryset = Catfact.objects.all()
    serializer_class = CatfactSerializer
    def destroy(self, request, *args, **kwargs):
        catfact = Catfact.objects.get(pk=self.kwargs["pk"])
        if not request.user == catfact.created_by:
            raise PermissionDenied("You cannot delete this catfact.")
        return super().destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        catfact = Catfact.objects.get(pk=self.kwargs["pk"])
        if not request.user == catfact.created_by:
            raise PermissionDenied("You cannot delete this catfact.")
        return super().update(request, *args, **kwargs)

# catfact/users/
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

# catfact/login/
class LoginView(APIView):
    permission_classes = ()
    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token":user.auth_token.key})
        else:
            return Response({"error":"Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)