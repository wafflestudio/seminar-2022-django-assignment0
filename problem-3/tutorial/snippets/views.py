from django import http
from django.views.decorators import csrf
from rest_framework import decorators
from rest_framework import parsers
from rest_framework import response
from rest_framework import status

from snippets import models
from snippets import serializers


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
