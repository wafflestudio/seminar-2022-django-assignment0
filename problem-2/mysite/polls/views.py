from django import http


def index(request: http.HttpRequest) -> http.HttpResponse:
    return http.HttpResponse("Hello, world. You're at the polls index.")
