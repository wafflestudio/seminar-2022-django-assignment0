from django import http
from django.views.decorators import csrf
from rest_framework import decorators
from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from rest_framework import views
from rest_framework import mixins
from rest_framework import generics

from snippets import models
from snippets import serializers

class SnippetList(generics.ListCreateAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer

"""
Class Based View : Rest framework GenericAPIView + MixIn 

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""
"""
Class Based View : Rest framework APIView 

class SnippetList(views.APIView):
    def get(self, request: http.HttpRequest, format = None) -> response.Response:
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)
        return response.Response(serializer.data)

    def post(self, request: http.HttpRequest, format=None) -> response.Response:
        serializer = serializers.SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(views.APIView):
    def get_object(self, pk):
        try:
            return models.Snippet.objects.get(pk=pk)
        except models.Snippet.DoesNotExist:
            raise http.Http404

    def get(self, request: http.HttpRequest, pk, format=None) -> http.HttpResponse:
        snippet = self.get_object(pk)
        serializer = serializers.SnippetSerializer(snippet)
        return response.Response(serializer.data)

    def put(self, request: http.HttpRequest, pk, format=None) -> http.HttpResponse:
        snippet = self.get_object(pk)
        serializer = serializers.SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: http.HttpRequest, pk, format=None) -> http.HttpResponse:
        snippet = self.get_object(pk)
        snippet.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
Function Based View

@csrf.csrf_exempt
@decorators.api_view(["GET", "POST"])
def snippet_list(request: http.HttpRequest, format = None) -> response.Response: # -> http.HttpResponse:
    if request.method == "GET":
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)
        return response.Response(serializer.data)
        # return http.JsonResponse(serializer.data, safe=False)
        
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = serializers.SnippetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            # return http.JsonResponse(serializer.data, status=201)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        # return http.JsonResponse(serializer.errors, status=400)


@csrf.csrf_exempt
@decorators.api_view(["GET", "POST", "DELETE"])
def snippet_detail(request: http.HttpRequest, pk: int, format = None) -> response.Response: # -> http.HttpResponse:
    try:
        snippet: models.Snippet = models.Snippet.objects.get(pk=pk)
    except models.Snippet.DoesNotExist:
        return response.Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        # return http.HttpResponse(status=404)

    if request.method == "GET":
        serializer = serializers.SnippetSerializer(snippet)
        return response.Response(serializer.data)
        # return http.JsonResponse(serializer.data, status=201)
        
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = serializers.SnippetSerializer(snippet, data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
            # return http.JsonResponse(serializer.data, status=201)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        # return http.JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return response.Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        # return http.HttpResponse(status=204)

"""