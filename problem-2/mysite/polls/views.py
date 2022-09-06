from multiprocessing import context
from django import http
from django import shortcuts
from django.template import loader

from polls import models


def index(request: http.HttpRequest) -> http.HttpResponse:
    latest_question_list = models.Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    # Normal
    # template = loader.get_template("polls/index.html")
    # return http.HttpResponse(template.render(context, request))
    
    # ShortCut
    return shortcuts.render(request, "polls/index.html", context)


def detail(request: http.HttpRequest, question_id: int) -> http.HttpResponse:
    # Normal
    # try: 
    #     question = models.Question.objects.get(pk=question_id)
    # except models.Question.DoesNotExist:
    #     raise http.Http404("Question does not exist")

    # ShortCut
    question = shortcuts.get_object_or_404(models.Question, pk=question_id)

    context = {
        "question": question
    }
    return shortcuts.render(request, "polls/detail.html", context)


def results(request: http.HttpRequest, question_id: int) -> http.HttpResponse:
    return http.HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request: http.HttpRequest, question_id: int) -> http.HttpResponse:
    return http.HttpResponse(f"You're voting on question {question_id}.")
