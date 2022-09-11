from django import http
from django.views.decorators import csrf
from rest_framework import parsers

from snippets import models
from snippets import serializers


@csrf.csrf_exempt
def snippet_list(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == "GET":
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)
        return http.JsonResponse(serializer.data, safe=False)
        
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = serializers.SnippetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return http.JsonResponse(serializer.data, status=201)
        return http.JsonResponse(serializer.errors, status=400)


@csrf.csrf_exempt
def snippet_detail(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    try:
        snippet: models.Snippet = models.Snippet.objects.get(pk=pk)
    except models.Snippet.DoesNotExist:
        return http.HttpResponse(status=404)

    if request.method == "GET":
        serializer = serializers.SnippetSerializer(snippet)
        return http.JsonResponse(serializer.data, status=201)
        
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = serializers.SnippetSerializer(snippet, data=data)

        if serializer.is_valid():
            serializer.save()
            return http.JsonResponse(serializer.data, status=201)
        return http.JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return http.HttpResponse(status=204)
